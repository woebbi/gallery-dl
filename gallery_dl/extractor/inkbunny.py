# -*- coding: utf-8 -*-

# Copyright 2020 Mike Fährmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Extractors for https://inkbunny.net/"""

from .common import Extractor, Message
from .. import text, exception
from ..cache import cache


BASE_PATTERN = r"(?:https?://)?(?:www\.)?inkbunny\.net"


class InkbunnyExtractor(Extractor):
    """Base class for inkbunny extractors"""
    category = "inkbunny"
    directory_fmt = ("{category}", "{username!l}")
    filename_fmt = "{submission_id} {file_id} {title}.{extension}"
    archive_fmt = "{file_id}"
    root = "https://inkbunny.net"

    def __init__(self, match):
        Extractor.__init__(self, match)
        self.api = InkbunnyAPI(self)

    def items(self):
        self.api.authenticate()
        to_bool = ("deleted", "favorite", "friends_only", "guest_block",
                   "hidden", "public", "scraps")

        for post in self.posts():
            post["date"] = text.parse_datetime(
                post["create_datetime"] + "00", "%Y-%m-%d %H:%M:%S.%f%z")
            post["tags"] = [kw["keyword_name"] for kw in post["keywords"]]
            post["ratings"] = [r["name"] for r in post["ratings"]]
            files = post["files"]

            for key in to_bool:
                if key in post:
                    post[key] = (post[key] == "t")

            del post["keywords"]
            del post["files"]

            yield Message.Directory, post
            for post["num"], file in enumerate(files, 1):
                post.update(file)
                post["deleted"] = (file["deleted"] == "t")
                post["date"] = text.parse_datetime(
                    file["create_datetime"] + "00", "%Y-%m-%d %H:%M:%S.%f%z")
                text.nameext_from_url(file["file_name"], post)

                url = file["file_url_full"]
                if "/private_files/" in url:
                    url += "?sid=" + self.api.session_id
                yield Message.Url, url, post


class InkbunnyUserExtractor(InkbunnyExtractor):
    """Extractor for inkbunny user profiles"""
    subcategory = "user"
    pattern = BASE_PATTERN + r"/(?!s/)(gallery/|scraps/)?(\w+)(?:$|[/?#])"
    test = (
        ("https://inkbunny.net/soina", {
            "pattern": r"https://[\w.]+\.metapix\.net/files/full"
                       r"/\d+/\d+_soina_.+",
            "range": "20-50",
            "keyword": {
                "date"         : "type:datetime",
                "deleted"      : bool,
                "file_id"      : "re:[0-9]+",
                "filename"     : r"re:[0-9]+_soina_\w+",
                "full_file_md5": "re:[0-9a-f]{32}",
                "mimetype"     : str,
                "submission_id": "re:[0-9]+",
                "user_id"      : "20969",
                "comments_count" : "re:[0-9]+",
                "deleted"        : bool,
                "favorite"       : bool,
                "favorites_count": "re:[0-9]+",
                "friends_only"   : bool,
                "guest_block"    : bool,
                "hidden"         : bool,
                "pagecount"      : "re:[0-9]+",
                "pools"          : list,
                "pools_count"    : int,
                "public"         : bool,
                "rating_id"      : "re:[0-9]+",
                "rating_name"    : str,
                "ratings"        : list,
                "scraps"         : bool,
                "tags"           : list,
                "title"          : str,
                "type_name"      : str,
                "username"       : "soina",
                "views"          : str,
            },
        }),
        ("https://inkbunny.net/gallery/soina", {
            "range": "1-25",
            "keyword": {"scraps": False},
        }),
        ("https://inkbunny.net/scraps/soina", {
            "range": "1-25",
            "keyword": {"scraps": True},
        }),
    )

    def __init__(self, match):
        kind, self.user = match.groups()
        if not kind:
            self.scraps = None
        elif kind[0] == "g":
            self.subcategory = "gallery"
            self.scraps = "no"
        else:
            self.subcategory = "scraps"
            self.scraps = "only"
        InkbunnyExtractor.__init__(self, match)

    def posts(self):
        orderby = self.config("orderby")
        params = {
            "username": self.user,
            "scraps"  : self.scraps,
            "orderby" : orderby,
        }
        if orderby and orderby.startswith("unread_"):
            params["unread_submissions"] = "yes"
        return self.api.search(params)


class InkbunnyFavoriteExtractor(InkbunnyExtractor):
    """Extractor for inkbunny user favorites"""
    subcategory = "favorite"
    pattern = BASE_PATTERN + r"/userfavorites_process\.php\?favs_user_id=(\d+)"
    test = (
        ("https://inkbunny.net/userfavorites_process.php?favs_user_id=20969", {
            "pattern": r"https://[\w.]+\.metapix\.net/files/full"
                       r"/\d+/\d+_\w+_.+",
            "range": "20-50",
        }),
    )

    def __init__(self, match):
        InkbunnyExtractor.__init__(self, match)
        self.user_id = match.group(1)

    def posts(self):
        orderby = self.config("orderby", "fav_datetime")
        params = {
            "favs_user_id": self.user_id,
            "orderby"     : orderby,
        }
        if orderby and orderby.startswith("unread_"):
            params["unread_submissions"] = "yes"
        return self.api.search(params)


class InkbunnyPostExtractor(InkbunnyExtractor):
    """Extractor for individual Inkbunny posts"""
    subcategory = "post"
    pattern = BASE_PATTERN + r"/s/(\d+)"
    test = (
        ("https://inkbunny.net/s/1829715", {
            "pattern": r"https://[\w.]+\.metapix\.net/files/full"
                       r"/2626/2626843_soina_dscn2296\.jpg",
            "content": "cf69d8dddf0822a12b4eef1f4b2258bd600b36c8",
        }),
        ("https://inkbunny.net/s/2044094", {
            "count": 4,
        }),
    )

    def __init__(self, match):
        InkbunnyExtractor.__init__(self, match)
        self.submission_id = match.group(1)

    def posts(self):
        submissions = self.api.detail(({"submission_id": self.submission_id},))
        if submissions[0] is None:
            raise exception.NotFoundError("submission")
        return submissions


class InkbunnyAPI():
    """Interface for the Inkunny API

    Ref: https://wiki.inkbunny.net/wiki/API
    """

    def __init__(self, extractor):
        self.extractor = extractor
        self.session_id = None

    def detail(self, submissions):
        """Get full details about submissions with the given IDs"""
        ids = {
            sub["submission_id"]: idx
            for idx, sub in enumerate(submissions)
        }
        params = {
            "submission_ids": ",".join(ids),
            "show_description": "yes",
        }

        submissions = [None] * len(ids)
        for sub in self._call("submissions", params)["submissions"]:
            submissions[ids[sub["submission_id"]]] = sub
        return submissions

    def search(self, params):
        """Perform a search"""
        return self._pagination_search(params)

    def set_allowed_ratings(self, nudity=True, sexual=True,
                            violence=True, strong_violence=True):
        """Change allowed submission ratings"""
        params = {
            "tag[2]": "yes" if nudity else "no",
            "tag[3]": "yes" if violence else "no",
            "tag[4]": "yes" if sexual else "no",
            "tag[5]": "yes" if strong_violence else "no",
        }
        self._call("userrating", params)

    def authenticate(self, invalidate=False):
        username, password = self.extractor._get_auth_info()
        if invalidate:
            _authenticate_impl.invalidate(username or "guest")
        if username:
            self.session_id = _authenticate_impl(self, username, password)
        else:
            self.session_id = _authenticate_impl(self, "guest", "")
            self.set_allowed_ratings()

    def _call(self, endpoint, params):
        url = "https://inkbunny.net/api_" + endpoint + ".php"
        params["sid"] = self.session_id
        data = self.extractor.request(url, params=params).json()

        if "error_code" in data:
            if str(data["error_code"]) == "2":
                self.authenticate(invalidate=True)
                return self._call(endpoint, params)
            raise exception.StopExtraction(data.get("error_message"))

        return data

    def _pagination_search(self, params):
        params["page"] = 1
        params["get_rid"] = "yes"
        params["submission_ids_only"] = "yes"

        while True:
            data = self._call("search", params)
            yield from self.detail(data["submissions"])

            if data["page"] >= data["pages_count"]:
                return
            if "get_rid" in params:
                del params["get_rid"]
                params["rid"] = data["rid"]
            params["page"] += 1


@cache(maxage=360*24*3600, keyarg=1)
def _authenticate_impl(api, username, password):
    api.extractor.log.info("Logging in as %s", username)

    url = "https://inkbunny.net/api_login.php"
    data = {"username": username, "password": password}
    data = api.extractor.request(url, method="POST", data=data).json()

    if "sid" not in data:
        raise exception.AuthenticationError(data.get("error_message"))
    return data["sid"]
