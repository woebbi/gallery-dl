#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Generate a Markdown document listing all supported sites"""

import os
import sys
import collections

import util
from gallery_dl import extractor


CATEGORY_MAP = {
    "2chan"          : "Futaba Channel",
    "35photo"        : "35PHOTO",
    "adultempire"    : "Adult Empire",
    "allgirlbooru"   : "All girl",
    "archivedmoe"    : "Archived.Moe",
    "archiveofsins"  : "Archive of Sins",
    "artstation"     : "ArtStation",
    "aryion"         : "Eka's Portal",
    "b4k"            : "arch.b4k.co",
    "baraag"         : "baraag",
    "bbc"            : "BBC",
    "bcy"            : "半次元",
    "comicvine"      : "Comic Vine",
    "deviantart"     : "DeviantArt",
    "drawfriends"    : "Draw Friends",
    "dynastyscans"   : "Dynasty Reader",
    "e621"           : "e621",
    "erome"          : "EroMe",
    "e-hentai"       : "E-Hentai",
    "exhentai"       : "ExHentai",
    "fallenangels"   : "Fallen Angels Scans",
    "fanbox"         : "pixivFANBOX",
    "fashionnova"    : "Fashion Nova",
    "furaffinity"    : "Fur Affinity",
    "hbrowse"        : "HBrowse",
    "hentai2read"    : "Hentai2Read",
    "hentaicosplays" : "Hentai Cosplay",
    "hentaifoundry"  : "Hentai Foundry",
    "hentaifox"      : "HentaiFox",
    "hentaihand"     : "HentaiHand",
    "hentaihere"     : "HentaiHere",
    "hentaiimg"      : "Hentai Image",
    "hitomi"         : "Hitomi.la",
    "idolcomplex"    : "Idol Complex",
    "illusioncardsbooru": "Illusion Game Cards",
    "imagebam"       : "ImageBam",
    "imagefap"       : "ImageFap",
    "imgbb"          : "ImgBB",
    "imgbox"         : "imgbox",
    "imagechest"     : "ImageChest",
    "imgth"          : "imgth",
    "imgur"          : "imgur",
    "kabeuchi"       : "かべうち",
    "kireicake"      : "Kirei Cake",
    "lineblog"       : "LINE BLOG",
    "livedoor"       : "livedoor Blog",
    "omgmiamiswimwear": "Omg Miami Swimwear",
    "mangadex"       : "MangaDex",
    "mangafox"       : "Manga Fox",
    "mangahere"      : "Manga Here",
    "mangakakalot"   : "MangaKakalot",
    "manganelo"      : "Manganato",
    "mangapark"      : "MangaPark",
    "mangasee"       : "MangaSee",
    "mastodon.social": "mastodon.social",
    "myhentaigallery": "My Hentai Gallery",
    "myportfolio"    : "Adobe Portfolio",
    "naverwebtoon"   : "NaverWebtoon",
    "nhentai"        : "nhentai",
    "nijie"          : "nijie",
    "nozomi"         : "Nozomi.la",
    "nsfwalbum"      : "NSFWalbum.com",
    "nyafuu"         : "Nyafuu Archive",
    "paheal"         : "rule #34",
    "photovogue"     : "PhotoVogue",
    "pornimagesxxx"  : "Porn Image",
    "powermanga"     : "PowerManga",
    "readcomiconline": "Read Comic Online",
    "rbt"            : "RebeccaBlackTech",
    "redgifs"        : "RedGIFs",
    "rule34"         : "Rule 34",
    "sankaku"        : "Sankaku Channel",
    "sankakucomplex" : "Sankaku Complex",
    "seiga"          : "Niconico Seiga",
    "seisoparty"     : "Seiso",
    "senmanga"       : "Sen Manga",
    "sensescans"     : "Sense-Scans",
    "sexcom"         : "Sex.com",
    "simplyhentai"   : "Simply Hentai",
    "slickpic"       : "SlickPic",
    "slideshare"     : "SlideShare",
    "smugmug"        : "SmugMug",
    "speakerdeck"    : "Speaker Deck",
    "subscribestar"  : "SubscribeStar",
    "tbib"           : "The Big ImageBoard",
    "thebarchive"    : "The /b/ Archive",
    "thecollection"  : "The /co/llection",
    "theloudbooru"   : "The Loud Booru",
    "tumblrgallery"  : "TumblrGallery",
    "vanillarock"    : "もえぴりあ",
    "vidyart"        : "/v/idyart",
    "vk"             : "VK",
    "vsco"           : "VSCO",
    "wakarimasen"    : "Wakarimasen Archive",
    "webtoons"       : "Webtoon",
    "wikiart"        : "WikiArt.org",
    "xhamster"       : "xHamster",
    "xvideos"        : "XVideos",
    "yandere"        : "yande.re",
}

SUBCATEGORY_MAP = {
    "doujin" : "Doujin",
    "gallery": "Galleries",
    "image"  : "individual Images",
    "index"  : "Site Index",
    "issue"  : "Comic Issues",
    "manga"  : "Manga",
    "popular": "Popular Images",
    "recent" : "Recent Images",
    "search" : "Search Results",
    "status" : "Images from Statuses",
    "tag"    : "Tag Searches",
    "user"   : "User Profiles",
    "watch"  : "Watches",
    "following"    : "",
    "related-pin"  : "related Pins",
    "related-board": "",

    "artstation": {
        "artwork": "Artwork Listings",
    },
    "desktopography": {
        "site": "",
    },
    "deviantart": {
        "stash": "Sta.sh",
        "watch-posts": "",
    },
    "hentaifoundry": {
        "story": "",
    },
    "instagram": {
        "posts": "",
        "saved": "Saved Posts",
        "tagged": "Tagged Posts",
    },
    "mangadex": {
        "feed" : "Followed Feed",
    },
    "newgrounds": {
        "art"  : "Art",
        "audio": "Audio",
        "media": "Media Files",
    },
    "pinterest": {
        "board": "",
        "pinit": "pin.it Links",
    },
    "pixiv": {
        "me"  : "pixiv.me Links",
        "pixivision": "pixivision",
        "work": "individual Images",
    },
    "sankaku": {
        "books": "Book Searches",
    },
    "smugmug": {
        "path": "Images from Users and Folders",
    },
    "twitter": {
        "media": "Media Timelines",
        "replies": "",
        "list-members": "List Members",
    },
    "wallhaven": {
        "collections": "",
    },
    "weasyl": {
        "journals"   : "",
        "submissions": "",
    },
    "wikiart": {
        "artists": "Artist Listings",
    },
}

BASE_MAP = {
    "foolfuuka"   : "FoolFuuka 4chan Archives",
    "foolslide"   : "FoOlSlide Instances",
    "gelbooru_v01": "Gelbooru Beta 0.1.11",
    "gelbooru_v02": "Gelbooru Beta 0.2",
    "moebooru"    : "Moebooru and MyImouto",
}

_OAUTH = '<a href="https://github.com/mikf/gallery-dl#oauth">OAuth</a>'
_COOKIES = '<a href="https://github.com/mikf/gallery-dl#cookies">Cookies</a>'
_APIKEY_DB = \
    '<a href="configuration.rst#extractorderpibooruapi-key">API Key</a>'
_APIKEY_WH = \
    '<a href="configuration.rst#extractorwallhavenapi-key">API Key</a>'
_APIKEY_WY = \
    '<a href="configuration.rst#extractorweasylapi-key">API Key</a>'

AUTH_MAP = {
    "aryion"         : "Supported",
    "baraag"         : _OAUTH,
    "danbooru"       : "Supported",
    "derpibooru"     : _APIKEY_DB,
    "deviantart"     : _OAUTH,
    "e621"           : "Supported",
    "e-hentai"       : "Supported",
    "exhentai"       : "Supported",
    "fanbox"         : _COOKIES,
    "fantia"         : _COOKIES,
    "flickr"         : _OAUTH,
    "furaffinity"    : _COOKIES,
    "idolcomplex"    : "Supported",
    "imgbb"          : "Supported",
    "inkbunny"       : "Supported",
    "instagram"      : "Supported",
    "kemonoparty"    : "Supported",
    "mangadex"       : "Supported",
    "mangoxo"        : "Supported",
    "mastodon.social": _OAUTH,
    "newgrounds"     : "Supported",
    "nijie"          : "Required",
    "patreon"        : _COOKIES,
    "pawoo"          : _OAUTH,
    "pillowfort"     : "Supported",
    "pinterest"      : _COOKIES,
    "pixiv"          : _OAUTH,
    "ponybooru"      : "API Key",
    "reddit"         : _OAUTH,
    "sankaku"        : "Supported",
    "seiga"          : "Required",
    "smugmug"        : _OAUTH,
    "subscribestar"  : "Supported",
    "tapas"          : "Supported",
    "tsumino"        : "Supported",
    "tumblr"         : _OAUTH,
    "twitter"        : "Supported",
    "wallhaven"      : _APIKEY_WH,
    "weasyl"         : _APIKEY_WY,
}

IGNORE_LIST = (
    "directlink",
    "oauth",
    "recursive",
    "test",
    "ytdl",
)


def domain(cls):
    """Return the web-domain related to an extractor class"""
    try:
        url = sys.modules[cls.__module__].__doc__.split()[-1]
        if url.startswith("http"):
            return url
    except Exception:
        pass

    if hasattr(cls, "root") and cls.root:
        return cls.root + "/"

    if hasattr(cls, "https"):
        scheme = "https" if cls.https else "http"
        netloc = cls.__doc__.split()[-1]
        return "{}://{}/".format(scheme, netloc)

    test = next(cls._get_tests(), None)
    if test:
        url = test[0]
        return url[:url.find("/", 8)+1]

    return ""


def category_text(c):
    """Return a human-readable representation of a category"""
    return CATEGORY_MAP.get(c) or c.capitalize()


def subcategory_text(c, sc):
    """Return a human-readable representation of a subcategory"""
    if c in SUBCATEGORY_MAP:
        scm = SUBCATEGORY_MAP[c]
        if sc in scm:
            return scm[sc]

    if sc in SUBCATEGORY_MAP:
        return SUBCATEGORY_MAP[sc]

    sc = sc.capitalize()
    return sc if sc.endswith("s") else sc + "s"


def category_key(c):
    """Generate sorting keys by category"""
    return category_text(c[0]).lower()


def subcategory_key(sc):
    """Generate sorting keys by subcategory"""
    return "A" if sc == "issue" else sc


def build_extractor_list():
    """Generate a sorted list of lists of extractor classes"""
    categories = collections.defaultdict(lambda: collections.defaultdict(list))
    default = categories[""]
    domains = {}

    for extr in extractor._list_classes():
        category = extr.category
        if category in IGNORE_LIST:
            continue
        if category:
            default[category].append(extr.subcategory)
            if category not in domains:
                domains[category] = domain(extr)
        else:
            base = categories[extr.basecategory]
            for category, root in extr.instances:
                base[category].append(extr.subcategory)
                if category not in domains:
                    domains[category] = root + "/"

    # sort subcategory lists
    for base in categories.values():
        for subcategories in base.values():
            subcategories.sort(key=subcategory_key)

    # add e-hentai.org
    default["e-hentai"] = default["exhentai"]
    domains["e-hentai"] = domains["exhentai"].replace("x", "-")

    # add hentai-cosplays sister sites (hentai-img, porn-images-xxx)
    default["hentaiimg"] = default["hentaicosplays"]
    domains["hentaiimg"] = "https://hentai-img.com/"

    default["pornimagesxxx"] = default["hentaicosplays"]
    domains["pornimagesxxx"] = "https://porn-images-xxx.com/"

    return categories, domains


# define table columns
COLUMNS = (
    ("Site", 20,
     lambda c, scs, d: category_text(c)),
    ("URL" , 35,
     lambda c, scs, d: d),
    ("Capabilities", 50,
     lambda c, scs, d: ", ".join(subcategory_text(c, sc) for sc in scs
                                 if subcategory_text(c, sc))),
    ("Authentication", 16,
     lambda c, scs, d: AUTH_MAP.get(c, "")),
)


def generate_output(columns, categories, domains):

    thead = []
    append = thead.append
    append("<tr>")
    for column in columns:
        append("    <th>" + column[0] + "</th>")
    append("</tr>")

    tbody = []
    append = tbody.append

    for name, base in categories.items():

        if name and base:
            name = BASE_MAP.get(name) or (name.capitalize() + " Instances")
            append('\n<tr>\n    <td colspan="4"><strong>' +
                   name + '</strong></td>\n</tr>')

        clist = sorted(base.items(), key=category_key)
        for category, subcategories in clist:
            append("<tr>")
            for column in columns:
                domain = domains[category]
                content = column[2](category, subcategories, domain)
                append("    <td>" + content + "</td>")
            append("</tr>")

    TEMPLATE = """# Supported Sites

<!-- auto-generated by {} -->
Consider all sites to be NSFW unless otherwise known.

<table>
<thead valign="bottom">
{}
</thead>
<tbody valign="top">
{}
</tbody>
</table>
"""
    return TEMPLATE.format(
        "/".join(os.path.normpath(__file__).split(os.sep)[-2:]),
        "\n".join(thead),
        "\n".join(tbody),
    )


categories, domains = build_extractor_list()
outfile = sys.argv[1] if len(sys.argv) > 1 else "supportedsites.md"
with open(util.path("docs", outfile), "w") as fp:
    fp.write(generate_output(COLUMNS, categories, domains))
