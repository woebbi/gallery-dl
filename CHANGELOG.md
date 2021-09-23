# Changelog

## Unreleased

## 1.18.4 - 2021-09-04
### Additions
- [420chan] add `thread` and `board` extractors ([#1773](https://github.com/mikf/gallery-dl/issues/1773))
- [deviantart] add `tag` extractor ([#1803](https://github.com/mikf/gallery-dl/issues/1803))
- [deviantart] add `comments` option ([#1800](https://github.com/mikf/gallery-dl/issues/1800))
- [deviantart] implement a `auto-watch` option ([#1466](https://github.com/mikf/gallery-dl/issues/1466), [#1757](https://github.com/mikf/gallery-dl/issues/1757))
- [foolfuuka] add `gallery` extractor ([#1785](https://github.com/mikf/gallery-dl/issues/1785))
- [furaffinity] expand URL pattern for searches ([#1780](https://github.com/mikf/gallery-dl/issues/1780))
- [kemonoparty] automatically generate required DDoS-GUARD cookies ([#1779](https://github.com/mikf/gallery-dl/issues/1779))
- [nhentai] add `favorite` extractor ([#1814](https://github.com/mikf/gallery-dl/issues/1814))
- [shopify] support windsorstore.com ([#1793](https://github.com/mikf/gallery-dl/issues/1793))
- [twitter] add `url` to user objects ([#1787](https://github.com/mikf/gallery-dl/issues/1787), [#1532](https://github.com/mikf/gallery-dl/issues/1532))
- [twitter] expand t.co links in user descriptions ([#1787](https://github.com/mikf/gallery-dl/issues/1787), [#1532](https://github.com/mikf/gallery-dl/issues/1532))
- show a warning if an extractor doesn`t yield any results ([#1428](https://github.com/mikf/gallery-dl/issues/1428), [#1759](https://github.com/mikf/gallery-dl/issues/1759))
- add a `j` format string conversion
- implement a `fallback` option ([#1770](https://github.com/mikf/gallery-dl/issues/1770))
- implement a `path-strip` option
### Changes
- [shopify] use API for product listings ([#1793](https://github.com/mikf/gallery-dl/issues/1793))
- update default User-Agent headers
### Fixes
- [deviantart] prevent exceptions for "empty" videos ([#1796](https://github.com/mikf/gallery-dl/issues/1796))
- [exhentai] improve image limits check ([#1808](https://github.com/mikf/gallery-dl/issues/1808))
- [inkbunny] fix extraction ([#1816](https://github.com/mikf/gallery-dl/issues/1816))
- [mangadex] prevent exceptions for manga without English title ([#1815](https://github.com/mikf/gallery-dl/issues/1815))
- [oauth] use defaults when config values are set to `null` ([#1778](https://github.com/mikf/gallery-dl/issues/1778))
- [pixiv] fix pixivision title extraction
- [reddit] delay RedditAPI initialization ([#1813](https://github.com/mikf/gallery-dl/issues/1813))
- [twitter] improve error reporting ([#1759](https://github.com/mikf/gallery-dl/issues/1759))
- [twitter] fix issue when filtering quote tweets ([#1792](https://github.com/mikf/gallery-dl/issues/1792))
- [twitter] fix `logout` option ([#1719](https://github.com/mikf/gallery-dl/issues/1719))
### Removals
- [deviantart] remove the "you need session cookies to download mature scraps" warning ([#1777](https://github.com/mikf/gallery-dl/issues/1777), [#1776](https://github.com/mikf/gallery-dl/issues/1776))
- [foolslide] remove entry for kobato.hologfx.com

## 1.18.3 - 2021-08-13
### Additions
- [bbc] add `width` option ([#1706](https://github.com/mikf/gallery-dl/issues/1706))
- [danbooru] add `external` option ([#1747](https://github.com/mikf/gallery-dl/issues/1747))
- [furaffinity] add `external` option ([#1492](https://github.com/mikf/gallery-dl/issues/1492))
- [luscious] add `gif` option ([#1701](https://github.com/mikf/gallery-dl/issues/1701))
- [newgrounds] add `format` option ([#1729](https://github.com/mikf/gallery-dl/issues/1729))
- [reactor] add `gif` option ([#1701](https://github.com/mikf/gallery-dl/issues/1701))
- [twitter] warn about suspended accounts ([#1759](https://github.com/mikf/gallery-dl/issues/1759))
- [twitter] extend `replies` option ([#1254](https://github.com/mikf/gallery-dl/issues/1254))
- [twitter] add option to log out and retry when blocked ([#1719](https://github.com/mikf/gallery-dl/issues/1719))
- [wikieat] add `thread` and `board` extractors ([#1699](https://github.com/mikf/gallery-dl/issues/1699), [#1607](https://github.com/mikf/gallery-dl/issues/1607))
### Changes
- [instagram] increase default delay between HTTP requests from 5s to 8s ([#1732](https://github.com/mikf/gallery-dl/issues/1732))
### Fixes
- [bbc] improve image dimensions ([#1706](https://github.com/mikf/gallery-dl/issues/1706))
- [bbc] support multi-page gallery listings ([#1730](https://github.com/mikf/gallery-dl/issues/1730))
- [behance] fix `collection` extraction
- [deviantart] get original files for GIF previews ([#1731](https://github.com/mikf/gallery-dl/issues/1731))
- [furaffinity] fix errors when using `category-transfer` ([#1274](https://github.com/mikf/gallery-dl/issues/1274))
- [hitomi] fix image URLs ([#1765](https://github.com/mikf/gallery-dl/issues/1765))
- [instagram] use custom User-Agent header for video downloads ([#1682](https://github.com/mikf/gallery-dl/issues/1682), [#1623](https://github.com/mikf/gallery-dl/issues/1623), [#1580](https://github.com/mikf/gallery-dl/issues/1580))
- [kemonoparty] fix username extraction ([#1750](https://github.com/mikf/gallery-dl/issues/1750))
- [kemonoparty] update file server domain ([#1764](https://github.com/mikf/gallery-dl/issues/1764))
- [newgrounds] fix errors when using `category-transfer` ([#1274](https://github.com/mikf/gallery-dl/issues/1274))
- [nsfwalbum] retry backend requests when extracting image URLs ([#1733](https://github.com/mikf/gallery-dl/issues/1733), [#1271](https://github.com/mikf/gallery-dl/issues/1271))
- [vk] prevent exception for empty/private profiles ([#1742](https://github.com/mikf/gallery-dl/issues/1742))

## 1.18.2 - 2021-07-23
### Additions
- [bbc] add `gallery` and `programme` extractors ([#1706](https://github.com/mikf/gallery-dl/issues/1706))
- [comicvine] add extractor ([#1712](https://github.com/mikf/gallery-dl/issues/1712))
- [kemonoparty] add `max-posts` option ([#1674](https://github.com/mikf/gallery-dl/issues/1674))
- [kemonoparty] parse `o` query parameters ([#1674](https://github.com/mikf/gallery-dl/issues/1674))
- [mastodon] add `reblogs` and `replies` options ([#1669](https://github.com/mikf/gallery-dl/issues/1669))
- [pixiv] add extractor for `pixivision` articles ([#1672](https://github.com/mikf/gallery-dl/issues/1672))
- [ytdl] add experimental extractor for sites supported by youtube-dl ([#1680](https://github.com/mikf/gallery-dl/issues/1680), [#878](https://github.com/mikf/gallery-dl/issues/878))
- extend `parent-metadata` functionality ([#1687](https://github.com/mikf/gallery-dl/issues/1687), [#1651](https://github.com/mikf/gallery-dl/issues/1651), [#1364](https://github.com/mikf/gallery-dl/issues/1364))
- add `archive-prefix` option ([#1711](https://github.com/mikf/gallery-dl/issues/1711))
- add `url-metadata` option ([#1659](https://github.com/mikf/gallery-dl/issues/1659), [#1073](https://github.com/mikf/gallery-dl/issues/1073))
### Changes
- [kemonoparty] skip duplicated patreon files ([#1689](https://github.com/mikf/gallery-dl/issues/1689), [#1667](https://github.com/mikf/gallery-dl/issues/1667))
- [mangadex] use custom User-Agent header ([#1535](https://github.com/mikf/gallery-dl/issues/1535))
### Fixes
- [hitomi] fix image URLs ([#1679](https://github.com/mikf/gallery-dl/issues/1679))
- [imagevenue] fix extraction ([#1677](https://github.com/mikf/gallery-dl/issues/1677))
- [instagram] fix extraction of `/explore/tags/` posts ([#1666](https://github.com/mikf/gallery-dl/issues/1666))
- [moebooru] fix `tags` ending with a `+` when logged in ([#1702](https://github.com/mikf/gallery-dl/issues/1702))
- [naverwebtoon] fix comic extraction
- [pururin] update domain and fix extraction
- [vk] improve metadata extraction and URL pattern ([#1691](https://github.com/mikf/gallery-dl/issues/1691))
- [downloader:ytdl] fix `outtmpl` setting for yt-dlp ([#1680](https://github.com/mikf/gallery-dl/issues/1680))

## 1.18.1 - 2021-07-04
### Additions
- [mangafox] add `manga` extractor ([#1633](https://github.com/mikf/gallery-dl/issues/1633))
- [mangasee] add `chapter` and `manga` extractors
- [mastodon] implement `text-posts` option ([#1569](https://github.com/mikf/gallery-dl/issues/1569), [#1669](https://github.com/mikf/gallery-dl/issues/1669))
- [seisoparty] add `user` and `post` extractors ([#1635](https://github.com/mikf/gallery-dl/issues/1635))
- implement conditional directories ([#1394](https://github.com/mikf/gallery-dl/issues/1394))
- add `T` format string conversion ([#1646](https://github.com/mikf/gallery-dl/issues/1646))
- document format string syntax
### Changes
- [twitter] set `retweet_id` for original retweets ([#1481](https://github.com/mikf/gallery-dl/issues/1481))
### Fixes
- [directlink] manually encode Referer URLs ([#1647](https://github.com/mikf/gallery-dl/issues/1647))
- [hiperdex] use domain from input URL
- [kemonoparty] fix `username` extraction ([#1652](https://github.com/mikf/gallery-dl/issues/1652))
- [kemonoparty] warn about missing DDoS-GUARD cookies
- [twitter] ensure guest tokens are returned as string ([#1665](https://github.com/mikf/gallery-dl/issues/1665))
- [webtoons] match arbitrary language codes ([#1643](https://github.com/mikf/gallery-dl/issues/1643))
- fix depth counter in UrlJob when specifying `-g` multiple times

## 1.18.0 - 2021-06-19
### Additions
- [foolfuuka] support `archive.wakarimasen.moe` ([#1595](https://github.com/mikf/gallery-dl/issues/1595))
- [mangadex] implement login with username & password ([#1535](https://github.com/mikf/gallery-dl/issues/1535))
- [mangadex] add extractor for a user's followed feed ([#1535](https://github.com/mikf/gallery-dl/issues/1535))
- [pixiv] support fetching privately followed users ([#1628](https://github.com/mikf/gallery-dl/issues/1628))
- implement conditional filenames ([#1394](https://github.com/mikf/gallery-dl/issues/1394))
- implement `filter` option for post processors ([#1460](https://github.com/mikf/gallery-dl/issues/1460))
- add `-T/--terminate` command-line option ([#1399](https://github.com/mikf/gallery-dl/issues/1399))
- add `-P/--postprocessor` command-line option ([#1583](https://github.com/mikf/gallery-dl/issues/1583))
### Changes
- [kemonoparty] update default filenames and archive IDs ([#1514](https://github.com/mikf/gallery-dl/issues/1514))
- [twitter] update default settings
  - change `retweets` and `quoted` options from `true` to `false`
  - change directory format for search results to the same as other extractors
- require an argument for `--clear-cache`
### Fixes
- [500px] update GraphQL queries
- [furaffinity] improve metadata extraction ([#1630](https://github.com/mikf/gallery-dl/issues/1630))
- [hitomi] update image URL generation ([#1637](https://github.com/mikf/gallery-dl/issues/1637))
- [idolcomplex] improve and fix pagination ([#1594](https://github.com/mikf/gallery-dl/issues/1594), [#1601](https://github.com/mikf/gallery-dl/issues/1601))
- [instagram] fix login ([#1631](https://github.com/mikf/gallery-dl/issues/1631))
- [instagram] update query hashes
- [mangadex] update to API v5 ([#1535](https://github.com/mikf/gallery-dl/issues/1535))
- [mangafox] improve URL pattern ([#1608](https://github.com/mikf/gallery-dl/issues/1608))
- [oauth] prevent exceptions when reporting errors ([#1603](https://github.com/mikf/gallery-dl/issues/1603))
- [philomena] fix tag escapes handling ([#1629](https://github.com/mikf/gallery-dl/issues/1629))
- [redgifs] update API server address ([#1632](https://github.com/mikf/gallery-dl/issues/1632))
- [sankaku] handle empty tags ([#1617](https://github.com/mikf/gallery-dl/issues/1617))
- [subscribestar] improve attachment filenames ([#1609](https://github.com/mikf/gallery-dl/issues/1609))
- [unsplash] update collections URL pattern ([#1627](https://github.com/mikf/gallery-dl/issues/1627))
- [postprocessor:metadata] handle dicts in `mode:tags` ([#1598](https://github.com/mikf/gallery-dl/issues/1598))

## 1.17.5 - 2021-05-30
### Additions
- [kemonoparty] add `metadata` option ([#1548](https://github.com/mikf/gallery-dl/issues/1548))
- [kemonoparty] add `type` metadata field ([#1556](https://github.com/mikf/gallery-dl/issues/1556))
- [mangapark] recognize v2.mangapark URLs ([#1578](https://github.com/mikf/gallery-dl/issues/1578))
- [patreon] extract user-defined `tags` ([#1539](https://github.com/mikf/gallery-dl/issues/1539), [#1540](https://github.com/mikf/gallery-dl/issues/1540))
- [pillowfort] implement login with username & password ([#846](https://github.com/mikf/gallery-dl/issues/846))
- [pillowfort] add `inline` and `external` options ([#846](https://github.com/mikf/gallery-dl/issues/846))
- [pixiv] implement `max-posts` option ([#1558](https://github.com/mikf/gallery-dl/issues/1558))
- [pixiv] add `metadata` option ([#1551](https://github.com/mikf/gallery-dl/issues/1551))
- [twitter] add `text-tweets` option ([#570](https://github.com/mikf/gallery-dl/issues/570))
- [weibo] extend `retweets` option ([#1542](https://github.com/mikf/gallery-dl/issues/1542))
- [postprocessor:ugoira] support using the `image2` demuxer ([#1550](https://github.com/mikf/gallery-dl/issues/1550))
- [postprocessor:ugoira] add `repeat-last-frame` option ([#1550](https://github.com/mikf/gallery-dl/issues/1550))
- support `XDG_CONFIG_HOME` ([#1545](https://github.com/mikf/gallery-dl/issues/1545))
- implement `parent-skip` and `"skip": "terminate"` options ([#1399](https://github.com/mikf/gallery-dl/issues/1399))
### Changes
- [twitter] resolve `t.co` URLs in `content` ([#1532](https://github.com/mikf/gallery-dl/issues/1532))
### Fixes
- [500px] update query hashes ([#1573](https://github.com/mikf/gallery-dl/issues/1573))
- [aryion] find text posts in `recursive=false` mode ([#1568](https://github.com/mikf/gallery-dl/issues/1568))
- [imagebam] fix extraction of NSFW images ([#1534](https://github.com/mikf/gallery-dl/issues/1534))
- [imgur] update URL patterns ([#1561](https://github.com/mikf/gallery-dl/issues/1561))
- [manganelo] update domain to `manganato.com`
- [reactor] skip deleted/empty posts
- [twitter] add missing retweet media entities ([#1555](https://github.com/mikf/gallery-dl/issues/1555))
- fix ISO 639-1 code for Japanese (`jp` -> `ja`)

## 1.17.4 - 2021-05-07
### Additions
- [gelbooru] add extractor for `/redirect.php` URLs ([#1530](https://github.com/mikf/gallery-dl/issues/1530))
- [inkbunny] add `favorite` extractor ([#1521](https://github.com/mikf/gallery-dl/issues/1521))
- add `output.skip` option
- add an optional argument to `--clear-cache` to select which cache entries to remove ([#1230](https://github.com/mikf/gallery-dl/issues/1230))
### Changes
- [pixiv] update `translated-tags` option ([#1507](https://github.com/mikf/gallery-dl/issues/1507))
  - rename to `tags`
  - accept `"japanese"`, `"translated"`, and `"original"` as values
### Fixes
- [500px] update query hashes
- [kemonoparty] fix download URLs ([#1514](https://github.com/mikf/gallery-dl/issues/1514))
- [imagebam] fix extraction
- [instagram] update query hashes
- [nozomi] update default archive-fmt for `tag` and `search` extractors ([#1529](https://github.com/mikf/gallery-dl/issues/1529))
- [pixiv] remove duplicate translated tags ([#1507](https://github.com/mikf/gallery-dl/issues/1507))
- [readcomiconline] change domain to `readcomiconline.li` ([#1517](https://github.com/mikf/gallery-dl/issues/1517))
- [sankaku] update invalid-token detection ([#1515](https://github.com/mikf/gallery-dl/issues/1515))
- fix crash when using `--no-download` with `--ugoira-conv` ([#1507](https://github.com/mikf/gallery-dl/issues/1507))

## 1.17.3 - 2021-04-25
### Additions
- [danbooru] add option for extended metadata extraction ([#1458](https://github.com/mikf/gallery-dl/issues/1458))
- [fanbox] add extractors ([#1459](https://github.com/mikf/gallery-dl/issues/1459))
- [fantia] add extractors ([#1459](https://github.com/mikf/gallery-dl/issues/1459))
- [gelbooru] add an option to extract notes ([#1457](https://github.com/mikf/gallery-dl/issues/1457))
- [hentaicosplays] add extractor ([#907](https://github.com/mikf/gallery-dl/issues/907), [#1473](https://github.com/mikf/gallery-dl/issues/1473), [#1483](https://github.com/mikf/gallery-dl/issues/1483))
- [instagram] add extractor for `tagged` posts ([#1439](https://github.com/mikf/gallery-dl/issues/1439))
- [naverwebtoon] ignore non-comic images
- [pixiv] also save untranslated tags when `translated-tags` is enabled ([#1501](https://github.com/mikf/gallery-dl/issues/1501))
- [shopify] support omgmiamiswimwear.com ([#1280](https://github.com/mikf/gallery-dl/issues/1280))
- implement `output.fallback` option
- add archive format to InfoJob output ([#875](https://github.com/mikf/gallery-dl/issues/875))
- build executables with SOCKS proxy support ([#1424](https://github.com/mikf/gallery-dl/issues/1424))
### Fixes
- [500px] update query hashes
- [8muses] fix JSON deobfuscation
- [artstation] download `/4k/` images ([#1422](https://github.com/mikf/gallery-dl/issues/1422))
- [deviantart] fix pagination for Eclipse results ([#1444](https://github.com/mikf/gallery-dl/issues/1444))
- [deviantart] improve folder name matching ([#1451](https://github.com/mikf/gallery-dl/issues/1451))
- [erome] skip deleted albums ([#1447](https://github.com/mikf/gallery-dl/issues/1447))
- [exhentai] fix image limit detection ([#1437](https://github.com/mikf/gallery-dl/issues/1437))
- [exhentai] restore `limits` option ([#1487](https://github.com/mikf/gallery-dl/issues/1487))
- [gelbooru] fix tag category extraction ([#1455](https://github.com/mikf/gallery-dl/issues/1455))
- [instagram] update query hashes
- [komikcast] fix extraction
- [simplyhentai] fix extraction
- [slideshare] fix extraction
- [webtoons] update agegate/GDPR cookies ([#1431](https://github.com/mikf/gallery-dl/issues/1431))
- fix `category-transfer` option
### Removals
- [yuki] remove module for yuki.la

## 1.17.2 - 2021-04-02
### Additions
- [deviantart] add support for posts from watched users ([#794](https://github.com/mikf/gallery-dl/issues/794))
- [manganelo] add `chapter` and `manga` extractors ([#1415](https://github.com/mikf/gallery-dl/issues/1415))
- [pinterest] add `search` extractor ([#1411](https://github.com/mikf/gallery-dl/issues/1411))
- [sankaku] add `tag_string` metadata field ([#1388](https://github.com/mikf/gallery-dl/issues/1388))
- [sankaku] add enumeration index for books ([#1388](https://github.com/mikf/gallery-dl/issues/1388))
- [tapas] add `series` and `episode` extractors ([#692](https://github.com/mikf/gallery-dl/issues/692))
- [tapas] implement login with username & password ([#692](https://github.com/mikf/gallery-dl/issues/692))
- [twitter] allow specifying a custom format for user results ([#1337](https://github.com/mikf/gallery-dl/issues/1337))
- [twitter] add extractor for direct image links ([#1417](https://github.com/mikf/gallery-dl/issues/1417))
- [vk] add support for albums ([#474](https://github.com/mikf/gallery-dl/issues/474))
### Fixes
- [aryion] unescape paths ([#1414](https://github.com/mikf/gallery-dl/issues/1414))
- [bcy] improve pagination
- [deviantart] update `watch` URL pattern ([#794](https://github.com/mikf/gallery-dl/issues/794))
- [deviantart] fix arguments for search/popular results ([#1408](https://github.com/mikf/gallery-dl/issues/1408))
- [deviantart] use fallback for `/intermediary/` URLs
- [exhentai] improve and simplify image limit checks
- [komikcast] fix extraction
- [pixiv] fix `favorite` URL pattern ([#1405](https://github.com/mikf/gallery-dl/issues/1405))
- [sankaku] simplify `pool` tags ([#1388](https://github.com/mikf/gallery-dl/issues/1388))
- [twitter] improve error message when trying to log in with 2FA ([#1409](https://github.com/mikf/gallery-dl/issues/1409))
- [twitter] don't use youtube-dl for cards when videos are disabled ([#1416](https://github.com/mikf/gallery-dl/issues/1416))

## 1.17.1 - 2021-03-19
### Additions
- [architizer] add `project` and `firm` extractors ([#1369](https://github.com/mikf/gallery-dl/issues/1369))
- [deviantart] add `watch` extractor ([#794](https://github.com/mikf/gallery-dl/issues/794))
- [exhentai] support `/tag/` URLs ([#1363](https://github.com/mikf/gallery-dl/issues/1363))
- [gelbooru_v01] support `drawfriends.booru.org`, `vidyart.booru.org`, and `tlb.booru.org` by default
- [nozomi] support `/index-N.html` URLs ([#1365](https://github.com/mikf/gallery-dl/issues/1365))
- [philomena] add generalized extractors for philomena sites ([#1379](https://github.com/mikf/gallery-dl/issues/1379))
- [philomena] support post URLs without `/images/`
- [twitter] implement `users` option ([#1337](https://github.com/mikf/gallery-dl/issues/1337))
- implement `parent-metadata` option ([#1364](https://github.com/mikf/gallery-dl/issues/1364))
### Changes
- [deviantart] revert previous changes to `extra` option ([#1356](https://github.com/mikf/gallery-dl/issues/1356), [#1387](https://github.com/mikf/gallery-dl/issues/1387))
### Fixes
- [exhentai] improve favorites count extraction ([#1360](https://github.com/mikf/gallery-dl/issues/1360))
- [gelbooru] update domain for video downloads ([#1368](https://github.com/mikf/gallery-dl/issues/1368))
- [hentaifox] improve image and metadata extraction ([#1366](https://github.com/mikf/gallery-dl/issues/1366), [#1378](https://github.com/mikf/gallery-dl/issues/1378))
- [imgur] fix and improve rate limit handling ([#1386](https://github.com/mikf/gallery-dl/issues/1386))
- [weasyl] improve favorites URL pattern ([#1374](https://github.com/mikf/gallery-dl/issues/1374))
- use type check before applying `browser` option ([#1358](https://github.com/mikf/gallery-dl/issues/1358))
- ensure `-s/--simulate` always prints filenames ([#1360](https://github.com/mikf/gallery-dl/issues/1360))
### Removals
- [hentaicafe]  remove module
- [hentainexus] remove module
- [mangareader] remove module
- [mangastream] remove module

## 1.17.0 - 2021-03-05
### Additions
- [cyberdrop] add support for `https://cyberdrop.me/` ([#1328](https://github.com/mikf/gallery-dl/issues/1328))
- [exhentai] add `metadata` option; extract more metadata from gallery pages ([#1325](https://github.com/mikf/gallery-dl/issues/1325))
- [hentaicafe] add `search` and `tag` extractors ([#1345](https://github.com/mikf/gallery-dl/issues/1345))
- [hentainexus] add `original` option ([#1322](https://github.com/mikf/gallery-dl/issues/1322))
- [instagram] support `/user/reels/` URLs ([#1329](https://github.com/mikf/gallery-dl/issues/1329))
- [naverwebtoon] add support for `https://comic.naver.com/` ([#1331](https://github.com/mikf/gallery-dl/issues/1331))
- [pixiv] add `translated-tags` option ([#1354](https://github.com/mikf/gallery-dl/issues/1354))
- [tbib] add support for `https://tbib.org/` ([#473](https://github.com/mikf/gallery-dl/issues/473), [#1082](https://github.com/mikf/gallery-dl/issues/1082))
- [tumblrgallery] add support for `https://tumblrgallery.xyz/` ([#1298](https://github.com/mikf/gallery-dl/issues/1298))
- [twitter] add extractor for followed users ([#1337](https://github.com/mikf/gallery-dl/issues/1337))
- [twitter] add option to download all media from conversations ([#1319](https://github.com/mikf/gallery-dl/issues/1319))
- [wallhaven] add `collections` extractor ([#1351](https://github.com/mikf/gallery-dl/issues/1351))
- [snap] allow access to user's .netrc for site authentication ([#1352](https://github.com/mikf/gallery-dl/issues/1352))
- add extractors for Gelbooru v0.1 sites ([#234](https://github.com/mikf/gallery-dl/issues/234), [#426](https://github.com/mikf/gallery-dl/issues/426), [#473](https://github.com/mikf/gallery-dl/issues/473), [#767](https://github.com/mikf/gallery-dl/issues/767), [#1238](https://github.com/mikf/gallery-dl/issues/1238))
- add `-E/--extractor-info` command-line option ([#875](https://github.com/mikf/gallery-dl/issues/875))
- add GitHub Actions workflow for building standalone executables ([#1312](https://github.com/mikf/gallery-dl/issues/1312))
- add `browser` and `headers` options ([#1117](https://github.com/mikf/gallery-dl/issues/1117))
- add option to use different youtube-dl forks ([#1330](https://github.com/mikf/gallery-dl/issues/1330))
- support using multiple input files at once ([#1353](https://github.com/mikf/gallery-dl/issues/1353))
### Changes
- [deviantart] extend `extra` option to also download embedded DeviantArt posts.
- [exhentai] rename metadata fields to match API results ([#1325](https://github.com/mikf/gallery-dl/issues/1325))
- [mangadex] use `api.mangadex.org` as default API server
- [mastodon] cache OAuth tokens ([#616](https://github.com/mikf/gallery-dl/issues/616))
- replace `wait-min` and `wait-max` with `sleep-request`
### Fixes
- [500px] skip unavailable photos ([#1335](https://github.com/mikf/gallery-dl/issues/1335))
- [komikcast] fix extraction
- [readcomiconline] download high quality image versions ([#1347](https://github.com/mikf/gallery-dl/issues/1347))
- [twitter] update GraphQL endpoints
- fix crash when `base-directory` is an empty string ([#1339](https://github.com/mikf/gallery-dl/issues/1339))
### Removals
- remove support for formerly deprecated options
- remove `cloudflare` module

## 1.16.5 - 2021-02-14
### Additions
- [behance] support `video` modules ([#1282](https://github.com/mikf/gallery-dl/issues/1282))
- [erome] add `album`, `user`, and `search` extractors ([#409](https://github.com/mikf/gallery-dl/issues/409))
- [hentaifox] support searching by group ([#1294](https://github.com/mikf/gallery-dl/issues/1294))
- [imgclick] add `image` extractor ([#1307](https://github.com/mikf/gallery-dl/issues/1307))
- [kemonoparty] extract inline images ([#1286](https://github.com/mikf/gallery-dl/issues/1286))
- [kemonoparty] support URLs with non-numeric user and post IDs ([#1303](https://github.com/mikf/gallery-dl/issues/1303))
- [pillowfort] add `user` and `post` extractors ([#846](https://github.com/mikf/gallery-dl/issues/846))
### Changes
- [kemonoparty] include `service` in directories and archive keys
- [pixiv] require a `refresh-token` to login ([#1304](https://github.com/mikf/gallery-dl/issues/1304))
- [snap] use `core18` as base
### Fixes
- [500px] update query hashes
- [deviantart] update parameters for `/browse/popular` ([#1267](https://github.com/mikf/gallery-dl/issues/1267))
- [deviantart] provide filename extension for original file downloads ([#1272](https://github.com/mikf/gallery-dl/issues/1272))
- [deviantart] fix `folders` option ([#1302](https://github.com/mikf/gallery-dl/issues/1302))
- [inkbunny] add `sid` parameter to private file downloads ([#1281](https://github.com/mikf/gallery-dl/issues/1281))
- [kemonoparty] fix absolute file URLs
- [mangadex] revert to `https://mangadex.org/api/` and add `api-server` option ([#1310](https://github.com/mikf/gallery-dl/issues/1310))
- [nsfwalbum] use fallback for deleted content ([#1259](https://github.com/mikf/gallery-dl/issues/1259))
- [sankaku] update `invalid token` detection ([#1309](https://github.com/mikf/gallery-dl/issues/1309))
- [slideshare] fix extraction
- [postprocessor:metadata] fix crash with `extension-format` ([#1285](https://github.com/mikf/gallery-dl/issues/1285))

## 1.16.4 - 2021-01-23
### Additions
- [furaffinity] add `descriptions` option ([#1231](https://github.com/mikf/gallery-dl/issues/1231))
- [kemonoparty] add `user` and `post` extractors ([#1216](https://github.com/mikf/gallery-dl/issues/1216))
- [nozomi] add `num` enumeration index ([#1239](https://github.com/mikf/gallery-dl/issues/1239))
- [photovogue] added portfolio extractor ([#1253](https://github.com/mikf/gallery-dl/issues/1253))
- [twitter] match `/i/user/ID` URLs
- [unsplash] add extractors ([#1197](https://github.com/mikf/gallery-dl/issues/1197))
- [vipr] add image extractor ([#1258](https://github.com/mikf/gallery-dl/issues/1258))
### Changes
- [derpibooru] use "Everything" filter by default ([#862](https://github.com/mikf/gallery-dl/issues/862))
### Fixes
- [derpibooru] update `date` parsing
- [foolfuuka] stop search when results are exhausted ([#1174](https://github.com/mikf/gallery-dl/issues/1174))
- [instagram] fix regex for `/saved` URLs ([#1251](https://github.com/mikf/gallery-dl/issues/1251))
- [mangadex] update API URLs
- [mangakakalot] fix extraction
- [newgrounds] fix flash file extraction ([#1257](https://github.com/mikf/gallery-dl/issues/1257))
- [sankaku] simplify login process
- [twitter] fix retries after hitting rate limit

## 1.16.3 - 2021-01-10
### Fixes
- fix crash when using a `dict` for `path-restrict`
- [postprocessor:metadata] sanitize custom filenames

## 1.16.2 - 2021-01-09
### Additions
- [derpibooru] add `search` and `gallery` extractors ([#862](https://github.com/mikf/gallery-dl/issues/862))
- [foolfuuka] add `board` and `search` extractors ([#1044](https://github.com/mikf/gallery-dl/issues/1044), [#1174](https://github.com/mikf/gallery-dl/issues/1174))
- [gfycat] add `date` metadata field ([#1138](https://github.com/mikf/gallery-dl/issues/1138))
- [pinterest] add support for getting all boards of a user ([#1205](https://github.com/mikf/gallery-dl/issues/1205))
- [sankaku] add support for book searches ([#1204](https://github.com/mikf/gallery-dl/issues/1204))
- [twitter] fetch media from pinned tweets ([#1203](https://github.com/mikf/gallery-dl/issues/1203))
- [wikiart] add extractor for single paintings ([#1233](https://github.com/mikf/gallery-dl/issues/1233))
- [downloader:http] add MIME type and signature for `.ico` files ([#1211](https://github.com/mikf/gallery-dl/issues/1211))
- add `d` format string conversion for timestamp values
- add `"ascii"` as a special `path-restrict` value
### Fixes
- [hentainexus] fix extraction ([#1234](https://github.com/mikf/gallery-dl/issues/1234))
- [instagram] categorize single highlight URLs as `highlights` ([#1222](https://github.com/mikf/gallery-dl/issues/1222))
- [redgifs] fix search results
- [twitter] fix login with username & password
- [twitter] fetch tweets from `homeConversation` entries

## 1.16.1 - 2020-12-27
### Additions
- [instagram] add `include` option ([#1180](https://github.com/mikf/gallery-dl/issues/1180))
- [pinterest] implement video support ([#1189](https://github.com/mikf/gallery-dl/issues/1189))
- [sankaku] reimplement login support ([#1176](https://github.com/mikf/gallery-dl/issues/1176), [#1182](https://github.com/mikf/gallery-dl/issues/1182))
- [sankaku] add support for sankaku.app URLs ([#1193](https://github.com/mikf/gallery-dl/issues/1193))
### Changes
- [e621] return pool posts in order ([#1195](https://github.com/mikf/gallery-dl/issues/1195))
- [hentaicafe] prefer title of `/hc.fyi/` pages ([#1106](https://github.com/mikf/gallery-dl/issues/1106))
- [hentaicafe] simplify default filenames
- [sankaku] normalize `created_at` metadata ([#1190](https://github.com/mikf/gallery-dl/issues/1190))
- [postprocessor:exec] do not add missing `{}` to command ([#1185](https://github.com/mikf/gallery-dl/issues/1185))
### Fixes
- [booru] improve error handling
- [instagram] warn about private profiles ([#1187](https://github.com/mikf/gallery-dl/issues/1187))
- [keenspot] improve redirect handling
- [mangadex] respect `chapter-reverse` settings ([#1194](https://github.com/mikf/gallery-dl/issues/1194))
- [pixiv] output debug message on failed login attempts ([#1192](https://github.com/mikf/gallery-dl/issues/1192))
- increase SQLite connection timeouts ([#1173](https://github.com/mikf/gallery-dl/issues/1173))
### Removals
- [mangapanda] remove module

## 1.16.0 - 2020-12-12
### Additions
- [booru] implement generalized extractors for `*booru` and `moebooru` sites
  - add support for sakugabooru.com ([#1136](https://github.com/mikf/gallery-dl/issues/1136))
  - add support for lolibooru.moe ([#1050](https://github.com/mikf/gallery-dl/issues/1050))
  - provide formattable `date` metadata fields ([#1138](https://github.com/mikf/gallery-dl/issues/1138))
- [postprocessor:metadata] add `event` and `filename` options ([#315](https://github.com/mikf/gallery-dl/issues/315), [#866](https://github.com/mikf/gallery-dl/issues/866), [#984](https://github.com/mikf/gallery-dl/issues/984))
- [postprocessor:exec] add `event` option ([#992](https://github.com/mikf/gallery-dl/issues/992))
### Changes
- [flickr] update default directories and improve metadata consistency ([#828](https://github.com/mikf/gallery-dl/issues/828))
- [sankaku] use API endpoints from `beta.sankakucomplex.com`
- [downloader:http] improve filename extension handling ([#776](https://github.com/mikf/gallery-dl/issues/776))
- replace all JPEG filename extensions with `jpg` by default
### Fixes
- [hentainexus] fix extraction ([#1166](https://github.com/mikf/gallery-dl/issues/1166))
- [instagram] rewrite ([#1113](https://github.com/mikf/gallery-dl/issues/1113), [#1122](https://github.com/mikf/gallery-dl/issues/1122), [#1128](https://github.com/mikf/gallery-dl/issues/1128), [#1130](https://github.com/mikf/gallery-dl/issues/1130), [#1149](https://github.com/mikf/gallery-dl/issues/1149))
- [mangadex] handle external chapters ([#1154](https://github.com/mikf/gallery-dl/issues/1154))
- [nozomi] handle empty `date` fields  ([#1163](https://github.com/mikf/gallery-dl/issues/1163))
- [paheal] create directory for each post ([#1147](https://github.com/mikf/gallery-dl/issues/1147))
- [piczel] update API URLs
- [twitter] update image URL format ([#1145](https://github.com/mikf/gallery-dl/issues/1145))
- [twitter] improve `x-csrf-token` header handling ([#1170](https://github.com/mikf/gallery-dl/issues/1170))
- [webtoons] update `ageGate` cookies
### Removals
- [sankaku] remove login support

## 1.15.4 - 2020-11-27
### Fixes
- [2chan] skip external links
- [hentainexus] fix extraction ([#1125](https://github.com/mikf/gallery-dl/issues/1125))
- [mangadex] switch to API v2 ([#1129](https://github.com/mikf/gallery-dl/issues/1129))
- [mangapanda] use http://
- [mangoxo] fix extraction
- [reddit] skip invalid gallery items ([#1127](https://github.com/mikf/gallery-dl/issues/1127))

## 1.15.3 - 2020-11-13
### Additions
- [sankakucomplex] extract videos and embeds ([#308](https://github.com/mikf/gallery-dl/issues/308))
- [twitter] add support for lists ([#1096](https://github.com/mikf/gallery-dl/issues/1096))
- [postprocessor:metadata] accept string-lists for `content-format` ([#1080](https://github.com/mikf/gallery-dl/issues/1080))
- implement `modules` and `extension-map` options
### Fixes
- [500px] update query hashes
- [8kun] fix file URLs of older posts ([#1101](https://github.com/mikf/gallery-dl/issues/1101))
- [exhentai] update image URL parsing ([#1094](https://github.com/mikf/gallery-dl/issues/1094))
- [hentaifoundry] update `YII_CSRF_TOKEN` cookie handling ([#1083](https://github.com/mikf/gallery-dl/issues/1083))
- [hentaifoundry] use scheme from input URLs ([#1095](https://github.com/mikf/gallery-dl/issues/1095))
- [mangoxo] fix metadata extraction
- [paheal] fix extraction ([#1088](https://github.com/mikf/gallery-dl/issues/1088))
- collect post processors from `basecategory` entries ([#1084](https://github.com/mikf/gallery-dl/issues/1084))

## 1.15.2 - 2020-10-24
### Additions
- [pinterest] implement login support ([#1055](https://github.com/mikf/gallery-dl/issues/1055))
- [reddit] add `date` metadata field ([#1068](https://github.com/mikf/gallery-dl/issues/1068))
- [seiga] add metadata for single image downloads ([#1063](https://github.com/mikf/gallery-dl/issues/1063))
- [twitter] support media from Cards ([#937](https://github.com/mikf/gallery-dl/issues/937), [#1005](https://github.com/mikf/gallery-dl/issues/1005))
- [weasyl] support api-key authentication ([#1057](https://github.com/mikf/gallery-dl/issues/1057))
- add a `t` format string conversion for trimming whitespace ([#1065](https://github.com/mikf/gallery-dl/issues/1065))
### Fixes
- [blogger] handle URLs with specified width/height ([#1061](https://github.com/mikf/gallery-dl/issues/1061))
- [fallenangels] fix extraction of `.5` chapters
- [gelbooru] rewrite mp4 video URLs ([#1048](https://github.com/mikf/gallery-dl/issues/1048))
- [hitomi] fix image URLs and gallery URL pattern
- [mangadex] unescape more metadata fields ([#1066](https://github.com/mikf/gallery-dl/issues/1066))
- [mangahere] ensure download URLs have a scheme ([#1070](https://github.com/mikf/gallery-dl/issues/1070))
- [mangakakalot] ignore "Go Home" buttons in chapter pages
- [newgrounds] handle embeds without scheme ([#1033](https://github.com/mikf/gallery-dl/issues/1033))
- [newgrounds] provide fallback URLs for video downloads ([#1042](https://github.com/mikf/gallery-dl/issues/1042))
- [xhamster] fix user profile extraction

## 1.15.1 - 2020-10-11
### Additions
- [hentaicafe] add `manga_id` metadata field ([#1036](https://github.com/mikf/gallery-dl/issues/1036))
- [hentaifoundry] add support for stories ([#734](https://github.com/mikf/gallery-dl/issues/734))
- [hentaifoundry] add `include` option
- [newgrounds] extract image embeds ([#1033](https://github.com/mikf/gallery-dl/issues/1033))
- [nijie] add `include` option ([#1018](https://github.com/mikf/gallery-dl/issues/1018))
- [reactor] match URLs without subdomain ([#1053](https://github.com/mikf/gallery-dl/issues/1053))
- [twitter] extend `retweets` option ([#1026](https://github.com/mikf/gallery-dl/issues/1026))
- [weasyl] add extractors ([#977](https://github.com/mikf/gallery-dl/issues/977))
### Fixes
- [500px] update query hashes
- [behance] fix `collection` extraction
- [newgrounds] fix video extraction ([#1042](https://github.com/mikf/gallery-dl/issues/1042))
- [twitter] improve twitpic extraction ([#1019](https://github.com/mikf/gallery-dl/issues/1019))
- [weibo] handle posts with more than 9 images ([#926](https://github.com/mikf/gallery-dl/issues/926))
- [xvideos] fix `title` extraction
- fix crash when using `--download-archive` with `--no-skip` ([#1023](https://github.com/mikf/gallery-dl/issues/1023))
- fix issues with `blacklist`/`whitelist` defaults ([#1051](https://github.com/mikf/gallery-dl/issues/1051), [#1056](https://github.com/mikf/gallery-dl/issues/1056))
### Removals
- [kissmanga] remove module

## 1.15.0 - 2020-09-20
### Additions
- [deviantart] support watchers-only/paid deviations ([#995](https://github.com/mikf/gallery-dl/issues/995))
- [myhentaigallery] add gallery extractor ([#1001](https://github.com/mikf/gallery-dl/issues/1001))
- [twitter] support specifying users by ID ([#980](https://github.com/mikf/gallery-dl/issues/980))
- [twitter] support `/intent/user?user_id=…` URLs ([#980](https://github.com/mikf/gallery-dl/issues/980))
- add `--no-skip` command-line option ([#986](https://github.com/mikf/gallery-dl/issues/986))
- add `blacklist` and `whitelist` options ([#492](https://github.com/mikf/gallery-dl/issues/492), [#844](https://github.com/mikf/gallery-dl/issues/844))
- add `filesize-min` and `filesize-max` options ([#780](https://github.com/mikf/gallery-dl/issues/780))
- add `sleep-extractor` and `sleep-request` options ([#788](https://github.com/mikf/gallery-dl/issues/788))
- write skipped files to archive ([#550](https://github.com/mikf/gallery-dl/issues/550))
### Changes
- [exhentai] update wait time before original image downloads ([#978](https://github.com/mikf/gallery-dl/issues/978))
- [imgur] use new API endpoints for image/album data
- [tumblr] create directories for each post ([#965](https://github.com/mikf/gallery-dl/issues/965))
- support format string replacement fields in download archive paths ([#985](https://github.com/mikf/gallery-dl/issues/985))
- reduce wait time growth rate for HTTP retries from exponential to linear
### Fixes
- [500px] update query hash
- [aryion] improve post ID extraction ([#981](https://github.com/mikf/gallery-dl/issues/981), [#982](https://github.com/mikf/gallery-dl/issues/982))
- [danbooru] handle posts without `id` ([#1004](https://github.com/mikf/gallery-dl/issues/1004))
- [furaffinity] update download URL extraction ([#988](https://github.com/mikf/gallery-dl/issues/988))
- [imgur] fix image/album detection for galleries
- [postprocessor:zip] defer zip file creation ([#968](https://github.com/mikf/gallery-dl/issues/968))
### Removals
- [jaiminisbox] remove extractors
- [worldthree] remove extractors

## 1.14.5 - 2020-08-30
### Additions
- [aryion] add username/password support ([#960](https://github.com/mikf/gallery-dl/issues/960))
- [exhentai] add ability to specify a custom image limit ([#940](https://github.com/mikf/gallery-dl/issues/940))
- [furaffinity] add `search` extractor ([#915](https://github.com/mikf/gallery-dl/issues/915))
- [imgur] add `search` and `tag` extractors ([#934](https://github.com/mikf/gallery-dl/issues/934))
### Fixes
- [500px] fix extraction and update URL patterns ([#956](https://github.com/mikf/gallery-dl/issues/956))
- [aryion] update folder mime type list ([#945](https://github.com/mikf/gallery-dl/issues/945))
- [gelbooru] fix extraction without API
- [hentaihand] update to new site layout
- [hitomi] fix redirect processing
- [reddit] handle deleted galleries ([#953](https://github.com/mikf/gallery-dl/issues/953))
- [reddit] improve gallery extraction ([#955](https://github.com/mikf/gallery-dl/issues/955))

## 1.14.4 - 2020-08-15
### Additions
- [blogger] add `search` extractor ([#925](https://github.com/mikf/gallery-dl/issues/925))
- [blogger] support searching posts by labels ([#925](https://github.com/mikf/gallery-dl/issues/925))
- [inkbunny] add `user` and `post` extractors ([#283](https://github.com/mikf/gallery-dl/issues/283))
- [instagram] support `/reel/` URLs
- [pinterest] support `pinterest.co.uk` URLs ([#914](https://github.com/mikf/gallery-dl/issues/914))
- [reddit] support gallery posts ([#920](https://github.com/mikf/gallery-dl/issues/920))
- [subscribestar] extract attached media files ([#852](https://github.com/mikf/gallery-dl/issues/852))
### Fixes
- [blogger] improve error messages for missing posts/blogs ([#903](https://github.com/mikf/gallery-dl/issues/903))
- [exhentai] adjust image limit costs ([#940](https://github.com/mikf/gallery-dl/issues/940))
- [gfycat] skip malformed gfycat responses ([#902](https://github.com/mikf/gallery-dl/issues/902))
- [imgur] handle 403 overcapacity responses ([#910](https://github.com/mikf/gallery-dl/issues/910))
- [instagram] wait before GraphQL requests ([#901](https://github.com/mikf/gallery-dl/issues/901))
- [mangareader] fix extraction
- [mangoxo] fix login
- [pixnet] detect password-protected albums ([#177](https://github.com/mikf/gallery-dl/issues/177))
- [simplyhentai] fix `gallery_id` extraction
- [subscribestar] update `date` parsing
- [vsco] handle missing `description` fields
- [xhamster] fix extraction ([#917](https://github.com/mikf/gallery-dl/issues/917))
- allow `parent-directory` to work recursively ([#905](https://github.com/mikf/gallery-dl/issues/905))
- skip external OAuth tests ([#908](https://github.com/mikf/gallery-dl/issues/908))
### Removals
- [bobx] remove module

## 1.14.3 - 2020-07-18
### Additions
- [8muses] support `comics.8muses.com` URLs
- [artstation] add `following` extractor ([#888](https://github.com/mikf/gallery-dl/issues/888))
- [exhentai] add `domain` option ([#897](https://github.com/mikf/gallery-dl/issues/897))
- [gfycat] add `user` and `search` extractors
- [imgur] support all `/t/...` URLs ([#880](https://github.com/mikf/gallery-dl/issues/880))
- [khinsider] add `format` option ([#840](https://github.com/mikf/gallery-dl/issues/840))
- [mangakakalot] add `manga` and `chapter` extractors ([#876](https://github.com/mikf/gallery-dl/issues/876))
- [redgifs] support `gifsdeliverynetwork.com` URLs ([#874](https://github.com/mikf/gallery-dl/issues/874))
- [subscribestar] add `user` and `post` extractors ([#852](https://github.com/mikf/gallery-dl/issues/852))
- [twitter] add support for nitter.net URLs ([#890](https://github.com/mikf/gallery-dl/issues/890))
- add Zsh completion script ([#150](https://github.com/mikf/gallery-dl/issues/150))
### Fixes
- [gfycat] retry 404'ed videos on redgifs.com ([#874](https://github.com/mikf/gallery-dl/issues/874))
- [newgrounds] fix favorites extraction
- [patreon] yield images and attachments before post files ([#871](https://github.com/mikf/gallery-dl/issues/871))
- [reddit] fix AttributeError when using `recursion` ([#879](https://github.com/mikf/gallery-dl/issues/879))
- [twitter] raise proper exception if a user doesn't exist ([#891](https://github.com/mikf/gallery-dl/issues/891))
- defer directory creation ([#722](https://github.com/mikf/gallery-dl/issues/722))
- set pseudo extension for Metadata messages ([#865](https://github.com/mikf/gallery-dl/issues/865))
- prevent exception on Cloudflare challenges ([#868](https://github.com/mikf/gallery-dl/issues/868))

## 1.14.2 - 2020-06-27
### Additions
- [artstation] add `date` metadata field ([#839](https://github.com/mikf/gallery-dl/issues/839))
- [mastodon] add `date` metadata field ([#839](https://github.com/mikf/gallery-dl/issues/839))
- [pinterest] add support for board sections ([#835](https://github.com/mikf/gallery-dl/issues/835))
- [twitter] add extractor for liked tweets ([#837](https://github.com/mikf/gallery-dl/issues/837))
- [twitter] add option to filter media from quoted tweets ([#854](https://github.com/mikf/gallery-dl/issues/854))
- [weibo] add `date` metadata field to `status` objects ([#829](https://github.com/mikf/gallery-dl/issues/829))
### Fixes
- [aryion] fix user gallery extraction ([#832](https://github.com/mikf/gallery-dl/issues/832))
- [imgur] build directory paths for each file ([#842](https://github.com/mikf/gallery-dl/issues/842))
- [tumblr] prevent errors when using `reblogs=same-blog` ([#851](https://github.com/mikf/gallery-dl/issues/851))
- [twitter] always provide an `author` metadata field ([#831](https://github.com/mikf/gallery-dl/issues/831), [#833](https://github.com/mikf/gallery-dl/issues/833))
- [twitter] don't download video previews ([#833](https://github.com/mikf/gallery-dl/issues/833))
- [twitter] improve handling of deleted tweets ([#838](https://github.com/mikf/gallery-dl/issues/838))
- [twitter] fix search results ([#847](https://github.com/mikf/gallery-dl/issues/847))
- [twitter] improve handling of quoted tweets ([#854](https://github.com/mikf/gallery-dl/issues/854))
- fix config lookups when multiple locations are involved ([#843](https://github.com/mikf/gallery-dl/issues/843))
- improve output of `-K/--list-keywords` for parent extractors ([#825](https://github.com/mikf/gallery-dl/issues/825))
- call `flush()` after writing JSON in `DataJob()` ([#727](https://github.com/mikf/gallery-dl/issues/727))

## 1.14.1 - 2020-06-12
### Additions
- [furaffinity] add `artist_url` metadata field ([#821](https://github.com/mikf/gallery-dl/issues/821))
- [redgifs] add `user` and `search` extractors ([#724](https://github.com/mikf/gallery-dl/issues/724))
### Changes
- [deviantart] extend `extra` option; also search journals for sta.sh links ([#712](https://github.com/mikf/gallery-dl/issues/712))
- [twitter] rewrite; use new interface ([#806](https://github.com/mikf/gallery-dl/issues/806), [#740](https://github.com/mikf/gallery-dl/issues/740))
### Fixes
- [kissmanga] work around CAPTCHAs ([#818](https://github.com/mikf/gallery-dl/issues/818))
- [nhentai] fix extraction ([#819](https://github.com/mikf/gallery-dl/issues/819))
- [webtoons] generalize comic extraction code ([#820](https://github.com/mikf/gallery-dl/issues/820))

## 1.14.0 - 2020-05-31
### Additions
- [imagechest] add new extractor for imgchest.com ([#750](https://github.com/mikf/gallery-dl/issues/750))
- [instagram] add `post_url`, `tags`, `location`, `tagged_users` metadata ([#743](https://github.com/mikf/gallery-dl/issues/743))
- [redgifs] add image extractor ([#724](https://github.com/mikf/gallery-dl/issues/724))
- [webtoons] add new extractor for webtoons.com ([#761](https://github.com/mikf/gallery-dl/issues/761))
- implement `--write-pages` option ([#736](https://github.com/mikf/gallery-dl/issues/736))
- extend `path-restrict` option ([#662](https://github.com/mikf/gallery-dl/issues/662))
- implement `path-replace` option ([#662](https://github.com/mikf/gallery-dl/issues/662), [#755](https://github.com/mikf/gallery-dl/issues/755))
- make `path` and `keywords` available in logging messages ([#574](https://github.com/mikf/gallery-dl/issues/574), [#575](https://github.com/mikf/gallery-dl/issues/575))
### Changes
- [danbooru] change default value of `ugoira` to `false`
- [downloader:ytdl] change default value of `forward-cookies` to `false`
- [downloader:ytdl] fix file extensions when merging into `.mkv` ([#720](https://github.com/mikf/gallery-dl/issues/720))
- write OAuth tokens to cache ([#616](https://github.com/mikf/gallery-dl/issues/616))
- use `%APPDATA%\gallery-dl` for config files and cache on Windows
- use `util.Formatter` for formatting logging messages
- reuse HTTP connections from parent extractors
### Fixes
- [deviantart] use private access tokens for Journals ([#738](https://github.com/mikf/gallery-dl/issues/738))
- [gelbooru] simplify and fix pool extraction
- [imgur] fix extraction of animated images without `mp4` entry
- [imgur] treat `/t/unmuted/` URLs as galleries
- [instagram] fix login with username & password ([#756](https://github.com/mikf/gallery-dl/issues/756), [#771](https://github.com/mikf/gallery-dl/issues/771), [#797](https://github.com/mikf/gallery-dl/issues/797), [#803](https://github.com/mikf/gallery-dl/issues/803))
- [reddit] don't send OAuth headers for file downloads ([#729](https://github.com/mikf/gallery-dl/issues/729))
- fix/improve Cloudflare bypass code ([#728](https://github.com/mikf/gallery-dl/issues/728), [#757](https://github.com/mikf/gallery-dl/issues/757))
- reset filenames on empty file extensions ([#733](https://github.com/mikf/gallery-dl/issues/733))

## 1.13.6 - 2020-05-02
### Additions
- [patreon] respect filters and sort order in query parameters ([#711](https://github.com/mikf/gallery-dl/issues/711))
- [speakerdeck] add a new extractor for speakerdeck.com ([#726](https://github.com/mikf/gallery-dl/issues/726))
- [twitter] add `replies` option ([#705](https://github.com/mikf/gallery-dl/issues/705))
- [weibo] add `videos` option
- [downloader:http] add MIME types for `.psd` files ([#714](https://github.com/mikf/gallery-dl/issues/714))
### Fixes
- [artstation] improve embed extraction ([#720](https://github.com/mikf/gallery-dl/issues/720))
- [deviantart] limit API wait times ([#721](https://github.com/mikf/gallery-dl/issues/721))
- [newgrounds] fix URLs produced by the `following` extractor ([#684](https://github.com/mikf/gallery-dl/issues/684))
- [patreon] improve file hash extraction ([#713](https://github.com/mikf/gallery-dl/issues/713))
- [vsco] fix user gallery extraction
- fix/improve Cloudflare bypass code ([#728](https://github.com/mikf/gallery-dl/issues/728))

## 1.13.5 - 2020-04-27
### Additions
- [500px] recognize `web.500px.com` URLs
- [aryion] support downloading from folders ([#694](https://github.com/mikf/gallery-dl/issues/694))
- [furaffinity] add extractor for followed users ([#515](https://github.com/mikf/gallery-dl/issues/515))
- [hitomi] add extractor for tag searches ([#697](https://github.com/mikf/gallery-dl/issues/697))
- [instagram] add `post_id` and `num` metadata fields ([#698](https://github.com/mikf/gallery-dl/issues/698))
- [newgrounds] add extractor for followed users ([#684](https://github.com/mikf/gallery-dl/issues/684))
- [patreon] recognize URLs with creator IDs ([#711](https://github.com/mikf/gallery-dl/issues/711))
- [twitter] add `reply` metadata field ([#705](https://github.com/mikf/gallery-dl/issues/705))
- [xhamster] recognize `xhamster.porncache.net` URLs ([#700](https://github.com/mikf/gallery-dl/issues/700))
### Fixes
- [gelbooru] improve post ID extraction in pool listings
- [hitomi] fix extraction of galleries without tags
- [jaiminisbox] update metadata decoding procedure ([#702](https://github.com/mikf/gallery-dl/issues/702))
- [mastodon] fix pagination ([#701](https://github.com/mikf/gallery-dl/issues/701))
- [mastodon] improve account searches ([#704](https://github.com/mikf/gallery-dl/issues/704))
- [patreon] fix hash extraction from download URLs ([#693](https://github.com/mikf/gallery-dl/issues/693))
- improve parameter extraction when solving Cloudflare challenges

## 1.13.4 - 2020-04-12
### Additions
- [aryion] add `gallery` and `post` extractors ([#390](https://github.com/mikf/gallery-dl/issues/390), [#673](https://github.com/mikf/gallery-dl/issues/673))
- [deviantart] detect and handle folders in sta.sh listings ([#659](https://github.com/mikf/gallery-dl/issues/659))
- [hentainexus] add `circle`, `event`, and `title_conventional` metadata fields ([#661](https://github.com/mikf/gallery-dl/issues/661))
- [hiperdex] add `artist` extractor ([#606](https://github.com/mikf/gallery-dl/issues/606))
- [mastodon] add access tokens for `mastodon.social` and `baraag.net` ([#665](https://github.com/mikf/gallery-dl/issues/665))
### Changes
- [deviantart] retrieve *all* download URLs through the OAuth API
- automatically read config files in PyInstaller executable directories ([#682](https://github.com/mikf/gallery-dl/issues/682))
### Fixes
- [deviantart] handle "Request blocked" errors ([#655](https://github.com/mikf/gallery-dl/issues/655))
- [deviantart] improve JPEG quality replacement pattern
- [hiperdex] fix extraction
- [mastodon] handle API rate limits ([#665](https://github.com/mikf/gallery-dl/issues/665))
- [mastodon] update OAuth credentials for pawoo.net ([#665](https://github.com/mikf/gallery-dl/issues/665))
- [myportfolio] fix extraction of galleries without title
- [piczel] fix extraction of single images
- [vsco] fix collection extraction
- [weibo] accept status URLs with non-numeric IDs ([#664](https://github.com/mikf/gallery-dl/issues/664))

## 1.13.3 - 2020-03-28
### Additions
- [instagram] Add support for user's saved medias ([#644](https://github.com/mikf/gallery-dl/issues/644))
- [nozomi] support multiple images per post ([#646](https://github.com/mikf/gallery-dl/issues/646))
- [35photo] add `tag` extractor
### Changes
- [mangadex] transform timestamps from `date` fields to datetime objects
### Fixes
- [deviantart] handle decode errors for `extended_fetch` results ([#655](https://github.com/mikf/gallery-dl/issues/655))
- [e621] fix bug in API rate limiting and improve pagination ([#651](https://github.com/mikf/gallery-dl/issues/651))
- [instagram] update pattern for user profile URLs
- [mangapark] fix metadata extraction
- [nozomi] sort search results ([#646](https://github.com/mikf/gallery-dl/issues/646))
- [piczel] fix extraction
- [twitter] fix typo in `x-twitter-auth-type` header ([#625](https://github.com/mikf/gallery-dl/issues/625))
- remove trailing dots from Windows directory names ([#647](https://github.com/mikf/gallery-dl/issues/647))
- fix crash with missing `stdout`/`stderr`/`stdin` handles ([#653](https://github.com/mikf/gallery-dl/issues/653))

## 1.13.2 - 2020-03-14
### Additions
- [furaffinity] extract more metadata
- [instagram] add `post_shortcode` metadata field ([#525](https://github.com/mikf/gallery-dl/issues/525))
- [kabeuchi] add extractor ([#561](https://github.com/mikf/gallery-dl/issues/561))
- [newgrounds] add extractor for favorited posts ([#394](https://github.com/mikf/gallery-dl/issues/394))
- [pixiv] implement `avatar` option ([#595](https://github.com/mikf/gallery-dl/issues/595), [#623](https://github.com/mikf/gallery-dl/issues/623))
- [twitter] add extractor for bookmarked Tweets ([#625](https://github.com/mikf/gallery-dl/issues/625))
### Fixes
- [bcy] reduce number of HTTP requests during data extraction
- [e621] update to new interface ([#635](https://github.com/mikf/gallery-dl/issues/635))
- [exhentai] handle incomplete MIME types ([#632](https://github.com/mikf/gallery-dl/issues/632))
- [hitomi] improve metadata extraction
- [mangoxo] fix login
- [newgrounds] improve error handling when extracting post data

## 1.13.1 - 2020-03-01
### Additions
- [hentaihand] add extractors ([#605](https://github.com/mikf/gallery-dl/issues/605))
- [hiperdex] add chapter and manga extractors ([#606](https://github.com/mikf/gallery-dl/issues/606))
- [oauth] implement option to write DeviantArt refresh-tokens to cache ([#616](https://github.com/mikf/gallery-dl/issues/616))
- [downloader:http] add more MIME types for `.bmp` and `.rar` files ([#621](https://github.com/mikf/gallery-dl/issues/621), [#628](https://github.com/mikf/gallery-dl/issues/628))
- warn about expired cookies
### Fixes
- [bcy] fix partial image URLs ([#613](https://github.com/mikf/gallery-dl/issues/613))
- [danbooru] fix Ugoira downloads and metadata
- [deviantart] check availability of `/intermediary/` URLs ([#609](https://github.com/mikf/gallery-dl/issues/609))
- [hitomi] follow multiple redirects & fix image URLs
- [piczel] improve and update
- [tumblr] replace `-` with ` ` in tag searches ([#611](https://github.com/mikf/gallery-dl/issues/611))
- [vsco] update gallery URL pattern
- fix `--verbose` and `--quiet` command-line options

## 1.13.0 - 2020-02-16
### Additions
- Support for
  - `furaffinity` - https://www.furaffinity.net/ ([#284](https://github.com/mikf/gallery-dl/issues/284))
  - `8kun`        - https://8kun.top/            ([#582](https://github.com/mikf/gallery-dl/issues/582))
  - `bcy`         - https://bcy.net/             ([#592](https://github.com/mikf/gallery-dl/issues/592))
- [blogger] implement video extraction ([#587](https://github.com/mikf/gallery-dl/issues/587))
- [oauth] add option to specify port number used by local server ([#604](https://github.com/mikf/gallery-dl/issues/604))
- [pixiv] add `rating` metadata field ([#595](https://github.com/mikf/gallery-dl/issues/595))
- [pixiv] recognize tags at the end of new bookmark URLs
- [reddit] add `videos` option
- [weibo] use youtube-dl to download from m3u8 manifests
- implement `parent-directory` option ([#551](https://github.com/mikf/gallery-dl/issues/551))
- extend filename formatting capabilities:
  - implement field name alternatives ([#525](https://github.com/mikf/gallery-dl/issues/525))
  - allow multiple "special" format specifiers per replacement field ([#595](https://github.com/mikf/gallery-dl/issues/595))
  - allow for numeric list and string indices
### Changes
- [reddit] handle reddit-hosted images and videos natively ([#551](https://github.com/mikf/gallery-dl/issues/551))
- [twitter] change default value for `videos` to `true`
### Fixes
- [cloudflare] unescape challenge URLs
- [deviantart] fix video extraction from `extended_fetch` results
- [hitomi] implement workaround for "broken" redirects
- [khinsider] fix and improve metadata extraction
- [patreon] filter duplicate files per post ([#590](https://github.com/mikf/gallery-dl/issues/590))
- [piczel] fix extraction
- [pixiv] fix user IDs for bookmarks API calls ([#596](https://github.com/mikf/gallery-dl/issues/596))
- [sexcom] fix image URLs
- [twitter] force old login page layout ([#584](https://github.com/mikf/gallery-dl/issues/584), [#598](https://github.com/mikf/gallery-dl/issues/598))
- [vsco] skip "invalid" entities
- improve functions to load/save cookies.txt files ([#586](https://github.com/mikf/gallery-dl/issues/586))
### Removals
- [yaplog] remove module

## 1.12.3 - 2020-01-19
### Additions
- [hentaifoundry] extract more metadata ([#565](https://github.com/mikf/gallery-dl/issues/565))
- [twitter] add option to extract TwitPic embeds ([#579](https://github.com/mikf/gallery-dl/issues/579))
- implement a post-processor module to compare file versions ([#530](https://github.com/mikf/gallery-dl/issues/530))
### Fixes
- [hitomi] update image URL generation
- [mangadex] revert domain to `mangadex.org`
- [pinterest] improve detection of invalid pin.it links
- [pixiv] update URL patterns for user profiles and bookmarks ([#568](https://github.com/mikf/gallery-dl/issues/568))
- [twitter] Fix stop before real end ([#573](https://github.com/mikf/gallery-dl/issues/573))
- remove temp files before downloading from fallback URLs
### Removals
- [erolord] remove extractor

## 1.12.2 - 2020-01-05
### Additions
- [deviantart] match new search/popular URLs ([#538](https://github.com/mikf/gallery-dl/issues/538))
- [deviantart] match `/favourites/all` URLs ([#555](https://github.com/mikf/gallery-dl/issues/555))
- [deviantart] add extractor for followed users ([#515](https://github.com/mikf/gallery-dl/issues/515))
- [pixiv] support listing followed users ([#515](https://github.com/mikf/gallery-dl/issues/515))
- [imagefap] handle beta.imagefap.com URLs ([#552](https://github.com/mikf/gallery-dl/issues/552))
- [postprocessor:metadata] add `directory` option ([#520](https://github.com/mikf/gallery-dl/issues/520))
### Fixes
- [artstation] fix search result pagination ([#537](https://github.com/mikf/gallery-dl/issues/537))
- [directlink] send Referer headers ([#536](https://github.com/mikf/gallery-dl/issues/536))
- [exhentai] restrict default directory name length ([#545](https://github.com/mikf/gallery-dl/issues/545))
- [mangadex] change domain to mangadex.cc ([#559](https://github.com/mikf/gallery-dl/issues/559))
- [mangahere] send `isAdult` cookies ([#556](https://github.com/mikf/gallery-dl/issues/556))
- [newgrounds] fix tags metadata extraction
- [pixiv] retry after rate limit errors ([#535](https://github.com/mikf/gallery-dl/issues/535))
- [twitter] handle quoted tweets ([#526](https://github.com/mikf/gallery-dl/issues/526))
- [twitter] handle API rate limits ([#526](https://github.com/mikf/gallery-dl/issues/526))
- [twitter] fix URLs forwarded to youtube-dl ([#540](https://github.com/mikf/gallery-dl/issues/540))
- prevent infinite recursion when spawning new extractors ([#489](https://github.com/mikf/gallery-dl/issues/489))
- improve output of `--list-keywords` for "parent" extractors ([#548](https://github.com/mikf/gallery-dl/issues/548))
- provide fallback for SQLite versions with missing `WITHOUT ROWID` support ([#553](https://github.com/mikf/gallery-dl/issues/553))

## 1.12.1 - 2019-12-22
### Additions
- [4chan] add extractor for entire boards ([#510](https://github.com/mikf/gallery-dl/issues/510))
- [realbooru] add extractors for pools, posts, and tag searches ([#514](https://github.com/mikf/gallery-dl/issues/514))
- [instagram] implement a `videos` option ([#521](https://github.com/mikf/gallery-dl/issues/521))
- [vsco] implement a `videos` option
- [postprocessor:metadata] implement a `bypost` option for downloading the metadata of an entire post ([#511](https://github.com/mikf/gallery-dl/issues/511))
### Changes
- [reddit] change the default value for `comments` to `0`
- [vsco] improve image resolutions
- make filesystem-related errors during file downloads non-fatal ([#512](https://github.com/mikf/gallery-dl/issues/512))
### Fixes
- [foolslide] add fallback for chapter data extraction
- [instagram] ignore errors during post-page extraction
- [patreon] avoid errors when fetching user info ([#508](https://github.com/mikf/gallery-dl/issues/508))
- [patreon] improve URL pattern for single posts
- [reddit] fix errors with `t1` submissions
- [vsco] fix user profile extraction … again
- [weibo] handle unavailable/deleted statuses
- [downloader:http] improve rate limit handling
- retain trailing zeroes in Cloudflare challenge answers

## 1.12.0 - 2019-12-08
### Additions
- [flickr] support 3k, 4k, 5k, and 6k photo sizes ([#472](https://github.com/mikf/gallery-dl/issues/472))
- [imgur] add extractor for subreddit links ([#500](https://github.com/mikf/gallery-dl/issues/500))
- [newgrounds] add extractors for `audio` listings and general `media` files ([#394](https://github.com/mikf/gallery-dl/issues/394))
- [newgrounds] implement login support ([#394](https://github.com/mikf/gallery-dl/issues/394))
- [postprocessor:metadata] implement a `extension-format` option ([#477](https://github.com/mikf/gallery-dl/issues/477))
- `--exec-after`
### Changes
- [deviantart] ensure consistent username capitalization ([#455](https://github.com/mikf/gallery-dl/issues/455))
- [directlink] split `{path}` into `{path}/{filename}.{extension}`
- [twitter] update metadata fields with user/author information
- [postprocessor:metadata] filter private entries & rename `format` to `content-format`
- Enable `cookies-update` by default
### Fixes
- [2chan] fix metadata extraction
- [behance] get images from 'media_collection' modules
- [bobx] fix image downloads by randomly generating session cookies ([#482](https://github.com/mikf/gallery-dl/issues/482))
- [deviantart] revert to getting download URLs from OAuth API calls ([#488](https://github.com/mikf/gallery-dl/issues/488))
- [deviantart] fix URL generation from '/extended_fetch' results ([#505](https://github.com/mikf/gallery-dl/issues/505))
- [flickr] adjust OAuth redirect URI ([#503](https://github.com/mikf/gallery-dl/issues/503))
- [hentaifox] fix extraction
- [imagefap] adapt to new image URL format
- [imgbb] fix error in galleries without user info ([#471](https://github.com/mikf/gallery-dl/issues/471))
- [instagram] prevent errors with missing 'video_url' fields ([#479](https://github.com/mikf/gallery-dl/issues/479))
- [nijie] fix `date` parsing
- [pixiv] match new search URLs ([#507](https://github.com/mikf/gallery-dl/issues/507))
- [plurk] fix comment pagination
- [sexcom] send specific Referer headers when downloading videos
- [twitter] fix infinite loops ([#499](https://github.com/mikf/gallery-dl/issues/499))
- [vsco] fix user profile and collection extraction ([#480](https://github.com/mikf/gallery-dl/issues/480))
- Fix Cloudflare DDoS protection bypass
### Removals
- `--abort-on-skip`

## 1.11.1 - 2019-11-09
### Fixes
- Fix inclusion of bash completion and man pages in source distributions

## 1.11.0 - 2019-11-08
### Additions
- Support for
  - `blogger` - https://www.blogger.com/ ([#364](https://github.com/mikf/gallery-dl/issues/364))
  - `nozomi`  - https://nozomi.la/       ([#388](https://github.com/mikf/gallery-dl/issues/388))
  - `issuu`   - https://issuu.com/       ([#413](https://github.com/mikf/gallery-dl/issues/413))
  - `naver`   - https://blog.naver.com/  ([#447](https://github.com/mikf/gallery-dl/issues/447))
- Extractor for `twitter` search results ([#448](https://github.com/mikf/gallery-dl/issues/448))
- Extractor for `deviantart` user profiles with configurable targets ([#377](https://github.com/mikf/gallery-dl/issues/377), [#419](https://github.com/mikf/gallery-dl/issues/419))
- `--ugoira-conv-lossless` ([#432](https://github.com/mikf/gallery-dl/issues/432))
- `cookies-update` option to allow updating cookies.txt files ([#445](https://github.com/mikf/gallery-dl/issues/445))
- Optional `cloudflare` and `video` installation targets ([#460](https://github.com/mikf/gallery-dl/issues/460))
- Allow executing commands with the `exec` post-processor after all files are downloaded ([#413](https://github.com/mikf/gallery-dl/issues/413), [#421](https://github.com/mikf/gallery-dl/issues/421))
### Changes
- Rewrite `imgur` using its public API ([#446](https://github.com/mikf/gallery-dl/issues/446))
- Rewrite `luscious` using GraphQL queries ([#457](https://github.com/mikf/gallery-dl/issues/457))
- Adjust default `nijie` filenames to match `pixiv`
- Change enumeration index for gallery extractors from `page` to `num`
- Return non-zero exit status when errors occurred
- Forward proxy settings to youtube-dl downloader
- Install bash completion script into `share/bash-completion/completions`
### Fixes
- Adapt to new `instagram` page layout when logged in ([#391](https://github.com/mikf/gallery-dl/issues/391))
- Support protected `twitter` videos ([#452](https://github.com/mikf/gallery-dl/issues/452))
- Extend `hitomi` URL pattern and fix gallery extraction
- Restore OAuth2 authentication error messages
- Miscellaneous fixes for `patreon` ([#444](https://github.com/mikf/gallery-dl/issues/444)), `deviantart` ([#455](https://github.com/mikf/gallery-dl/issues/455)), `sexcom` ([#464](https://github.com/mikf/gallery-dl/issues/464)), `imgur` ([#467](https://github.com/mikf/gallery-dl/issues/467)), `simplyhentai`

## 1.10.6 - 2019-10-11
### Additions
- `--exec` command-line option to specify a command to run after each file download ([#421](https://github.com/mikf/gallery-dl/issues/421))
### Changes
- Include titles in `gfycat` default filenames ([#434](https://github.com/mikf/gallery-dl/issues/434))
### Fixes
- Fetch working download URLs for `deviantart` ([#436](https://github.com/mikf/gallery-dl/issues/436))
- Various fixes and improvements for `yaplog` blogs ([#443](https://github.com/mikf/gallery-dl/issues/443))
- Fix image URL generation for `hitomi` galleries
- Miscellaneous fixes for `behance` and `xvideos`

## 1.10.5 - 2019-09-28
### Additions
- `instagram.highlights` option to include highlighted stories when downloading user profiles ([#329](https://github.com/mikf/gallery-dl/issues/329))
- Support for `/user/` URLs on `reddit` ([#350](https://github.com/mikf/gallery-dl/issues/350))
- Support for `imgur` user profiles and favorites ([#420](https://github.com/mikf/gallery-dl/issues/420))
- Additional metadata fields on `nijie`([#423](https://github.com/mikf/gallery-dl/issues/423))
### Fixes
- Improve handling of private `deviantart` artworks ([#414](https://github.com/mikf/gallery-dl/issues/414)) and 429 status codes ([#424](https://github.com/mikf/gallery-dl/issues/424))
- Prevent fatal errors when trying to open download-archive files ([#417](https://github.com/mikf/gallery-dl/issues/417))
- Detect and ignore unavailable videos on `weibo` ([#427](https://github.com/mikf/gallery-dl/issues/427))
- Update the `scope` of new `reddit` refresh-tokens ([#428](https://github.com/mikf/gallery-dl/issues/428))
- Fix inconsistencies with the `reddit.comments` option ([#429](https://github.com/mikf/gallery-dl/issues/429))
- Extend URL patterns for `hentaicafe` manga and `pixiv` artworks
- Improve detection of unavailable albums on `luscious` and `imgbb`
- Miscellaneous fixes for `tsumino`

## 1.10.4 - 2019-09-08
### Additions
- Support for
  - `lineblog` - https://www.lineblog.me/ ([#404](https://github.com/mikf/gallery-dl/issues/404))
  - `fuskator` - https://fuskator.com/    ([#407](https://github.com/mikf/gallery-dl/issues/407))
- `ugoira` option for `danbooru` to download pre-rendered ugoira animations ([#406](https://github.com/mikf/gallery-dl/issues/406))
### Fixes
- Download the correct files from `twitter` replies ([#403](https://github.com/mikf/gallery-dl/issues/403))
- Prevent crash when trying to use unavailable downloader modules ([#405](https://github.com/mikf/gallery-dl/issues/405))
- Fix `pixiv` authentication ([#411](https://github.com/mikf/gallery-dl/issues/411))
- Improve `exhentai` image limit checks
- Miscellaneous fixes for `hentaicafe`, `simplyhentai`, `tumblr`

## 1.10.3 - 2019-08-30
### Additions
- Provide `filename` metadata for all `deviantart` files ([#392](https://github.com/mikf/gallery-dl/issues/392), [#400](https://github.com/mikf/gallery-dl/issues/400))
- Implement a `ytdl.outtmpl` option to let youtube-dl handle filenames by itself ([#395](https://github.com/mikf/gallery-dl/issues/395))
- Support `seiga` mobile URLs ([#401](https://github.com/mikf/gallery-dl/issues/401))
### Fixes
- Extract more than the first 32 posts from `piczel` galleries ([#396](https://github.com/mikf/gallery-dl/issues/396))
- Fix filenames of archives created with `--zip` ([#397](https://github.com/mikf/gallery-dl/issues/397))
- Skip unavailable images and videos on `flickr` ([#398](https://github.com/mikf/gallery-dl/issues/398))
- Fix filesystem paths on Windows with Python 3.6 and lower ([#402](https://github.com/mikf/gallery-dl/issues/402))

## 1.10.2 - 2019-08-23
### Additions
- Support for `instagram` stories and IGTV ([#371](https://github.com/mikf/gallery-dl/issues/371), [#373](https://github.com/mikf/gallery-dl/issues/373))
- Support for individual `imgbb` images ([#363](https://github.com/mikf/gallery-dl/issues/363))
- `deviantart.quality` option to set the JPEG compression quality for newer images ([#369](https://github.com/mikf/gallery-dl/issues/369))
- `enumerate` option for `extractor.skip` ([#306](https://github.com/mikf/gallery-dl/issues/306))
- `adjust-extensions` option to control filename extension adjustments
- `path-remove` option to remove control characters etc. from filesystem paths
### Changes
- Rename `restrict-filenames` to `path-restrict`
- Adjust `pixiv` metadata and default filename format ([#366](https://github.com/mikf/gallery-dl/issues/366))
  - Set `filename` to `"{category}_{user[id]}_{id}{suffix}.{extension}"` to restore the old default
- Improve and optimize directory and filename generation
### Fixes
- Allow the `classify` post-processor to handle files with unknown filename extension ([#138](https://github.com/mikf/gallery-dl/issues/138))
- Fix rate limit handling for OAuth APIs ([#368](https://github.com/mikf/gallery-dl/issues/368))
- Fix artwork and scraps extraction on `deviantart` ([#376](https://github.com/mikf/gallery-dl/issues/376), [#392](https://github.com/mikf/gallery-dl/issues/392))
- Distinguish between `imgur` album and gallery URLs ([#380](https://github.com/mikf/gallery-dl/issues/380))
- Prevent crash when using `--ugoira-conv` ([#382](https://github.com/mikf/gallery-dl/issues/382))
- Handle multi-image posts on `patreon` ([#383](https://github.com/mikf/gallery-dl/issues/383))
- Miscellaneous fixes for `*reactor`, `simplyhentai`

## 1.10.1 - 2019-08-02
## Fixes
- Use the correct domain for exhentai.org input URLs

## 1.10.0 - 2019-08-01
### Warning
- Prior to version 1.10.0 all cache files were created world readable (mode `644`)
  leading to possible sensitive information disclosure on multi-user systems
- It is recommended to restrict access permissions of already existing files
  (`/tmp/.gallery-dl.cache`) with `chmod 600`
- Windows users should not be affected
### Additions
- Support for
  - `vsco`        - https://vsco.co/             ([#331](https://github.com/mikf/gallery-dl/issues/331))
  - `imgbb`       - https://imgbb.com/           ([#361](https://github.com/mikf/gallery-dl/issues/361))
  - `adultempire` - https://www.adultempire.com/ ([#340](https://github.com/mikf/gallery-dl/issues/340))
- `restrict-filenames` option to create Windows-compatible filenames on any platform ([#348](https://github.com/mikf/gallery-dl/issues/348))
- `forward-cookies` option to control cookie forwarding to youtube-dl ([#352](https://github.com/mikf/gallery-dl/issues/352))
### Changes
- The default cache file location on non-Windows systems is now
  - `$XDG_CACHE_HOME/gallery-dl/cache.sqlite3` or
  - `~/.cache/gallery-dl/cache.sqlite3`
- New cache files are created with mode `600`
- `exhentai` extractors will always use `e-hentai.org` as domain
### Fixes
- Better handling of `exhentai` image limits and errors ([#356](https://github.com/mikf/gallery-dl/issues/356), [#360](https://github.com/mikf/gallery-dl/issues/360))
- Try to prevent ZIP file corruption ([#355](https://github.com/mikf/gallery-dl/issues/355))
- Miscellaneous fixes for `behance`, `ngomik`

## 1.9.0 - 2019-07-19
### Additions
- Support for
  - `erolord` - http://erolord.com/ ([#326](https://github.com/mikf/gallery-dl/issues/326))
- Add login support for `instagram` ([#195](https://github.com/mikf/gallery-dl/issues/195))
- Add `--no-download` and `extractor.*.download` disable file downloads ([#220](https://github.com/mikf/gallery-dl/issues/220))
- Add `-A/--abort` to specify the number of consecutive download skips before aborting
- Interpret `-1` as infinite retries ([#300](https://github.com/mikf/gallery-dl/issues/300))
- Implement custom log message formats per log-level ([#304](https://github.com/mikf/gallery-dl/issues/304))
- Implement an `mtime` post-processor that sets file modification times according to metadata fields ([#332](https://github.com/mikf/gallery-dl/issues/332))
- Implement a `twitter.content` option to enable tweet text extraction ([#333](https://github.com/mikf/gallery-dl/issues/333), [#338](https://github.com/mikf/gallery-dl/issues/338))
- Enable `date-min/-max/-format` options for `tumblr` ([#337](https://github.com/mikf/gallery-dl/issues/337))
### Changes
- Set file modification times according to their `Last-Modified` header when downloading ([#236](https://github.com/mikf/gallery-dl/issues/236), [#277](https://github.com/mikf/gallery-dl/issues/277))
  - Use `--no-mtime` or `downloader.*.mtime` to disable this behavior
- Duplicate download URLs are no longer silently ignored (controllable with `extractor.*.image-unique`)
- Deprecate `--abort-on-skip`
### Fixes
- Retry downloads on OpenSSL exceptions ([#324](https://github.com/mikf/gallery-dl/issues/324))
- Ignore unavailable pins on `sexcom` instead of raising an exception ([#325](https://github.com/mikf/gallery-dl/issues/325))
- Use Firefox's SSL/TLS ciphers to prevent Cloudflare CAPTCHAs ([#342](https://github.com/mikf/gallery-dl/issues/342))
- Improve folder name matching on `deviantart` ([#343](https://github.com/mikf/gallery-dl/issues/343))
- Forward cookies to `youtube-dl` to allow downloading private videos
- Miscellaneous fixes for `35photo`, `500px`, `newgrounds`, `simplyhentai`

## 1.8.7 - 2019-06-28
### Additions
- Support for
  - `vanillarock` - https://vanilla-rock.com/ ([#254](https://github.com/mikf/gallery-dl/issues/254))
  - `nsfwalbum`   - https://nsfwalbum.com/    ([#287](https://github.com/mikf/gallery-dl/issues/287))
- `artist` and `tags` metadata for `hentaicafe` ([#238](https://github.com/mikf/gallery-dl/issues/238))
- `description` metadata for `instagram` ([#310](https://github.com/mikf/gallery-dl/issues/310))
- Format string option to replace a substring with another - `R<old>/<new>/` ([#318](https://github.com/mikf/gallery-dl/issues/318))
### Changes
- Delete empty archives created by the `zip` post-processor ([#316](https://github.com/mikf/gallery-dl/issues/316))
### Fixes
- Handle `hitomi` Game CG galleries correctly ([#321](https://github.com/mikf/gallery-dl/issues/321))
- Miscellaneous fixes for `deviantart`, `hitomi`, `pururin`, `kissmanga`, `keenspot`, `mangoxo`, `imagefap`

## 1.8.6 - 2019-06-14
### Additions
- Support for
  - `slickpic` - https://www.slickpic.com/ ([#249](https://github.com/mikf/gallery-dl/issues/249))
  - `xhamster` - https://xhamster.com/     ([#281](https://github.com/mikf/gallery-dl/issues/281))
  - `pornhub`  - https://www.pornhub.com/  ([#282](https://github.com/mikf/gallery-dl/issues/282))
  - `8muses`   - https://www.8muses.com/   ([#305](https://github.com/mikf/gallery-dl/issues/305))
- `extra` option for `deviantart` to download Sta.sh content linked in description texts ([#302](https://github.com/mikf/gallery-dl/issues/302))
### Changes
- Detect `directlink` URLs with upper case filename extensions ([#296](https://github.com/mikf/gallery-dl/issues/296))
### Fixes
- Improved error handling for `tumblr` API calls ([#297](https://github.com/mikf/gallery-dl/issues/297))
- Fixed extraction of `livedoor` blogs ([#301](https://github.com/mikf/gallery-dl/issues/301))
- Fixed extraction of special `deviantart` Sta.sh items ([#307](https://github.com/mikf/gallery-dl/issues/307))
- Fixed pagination for specific `keenspot` comics

## 1.8.5 - 2019-06-01
### Additions
- Support for
  - `keenspot`       - http://keenspot.com/           ([#223](https://github.com/mikf/gallery-dl/issues/223))
  - `sankakucomplex` - https://www.sankakucomplex.com ([#258](https://github.com/mikf/gallery-dl/issues/258))
- `folders` option for `deviantart` to add a list of containing folders to each file ([#276](https://github.com/mikf/gallery-dl/issues/276))
- `captcha` option for `kissmanga` and `readcomiconline` to control CAPTCHA handling ([#279](https://github.com/mikf/gallery-dl/issues/279))
- `filename` metadata for files downloaded with youtube-dl ([#291](https://github.com/mikf/gallery-dl/issues/291))
### Changes
- Adjust `wallhaven` extractors to new page layout:
  - use API and add `api-key` option
  - removed traditional login support
- Provide original filenames for `patreon` downloads ([#268](https://github.com/mikf/gallery-dl/issues/268))
- Use e-hentai.org or exhentai.org depending on input URL ([#278](https://github.com/mikf/gallery-dl/issues/278))
### Fixes
- Fix pagination over `sankaku` popular listings ([#265](https://github.com/mikf/gallery-dl/issues/265))
- Fix folder and collection extraction on `deviantart` ([#271](https://github.com/mikf/gallery-dl/issues/271))
- Detect "AreYouHuman" redirects on `readcomiconline` ([#279](https://github.com/mikf/gallery-dl/issues/279))
- Miscellaneous fixes for `hentainexus`, `livedoor`, `ngomik`

## 1.8.4 - 2019-05-17
### Additions
- Support for
  - `patreon`     - https://www.patreon.com/ ([#226](https://github.com/mikf/gallery-dl/issues/226))
  - `hentainexus` - https://hentainexus.com/ ([#256](https://github.com/mikf/gallery-dl/issues/256))
- `date` metadata fields for `pixiv` ([#248](https://github.com/mikf/gallery-dl/issues/248)), `instagram` ([#250](https://github.com/mikf/gallery-dl/issues/250)), `exhentai`, and `newgrounds`
### Changes
- Improved `flickr` metadata and video extraction ([#246](https://github.com/mikf/gallery-dl/issues/246))
### Fixes
- Download original GIF animations from `deviantart` ([#242](https://github.com/mikf/gallery-dl/issues/242))
- Ignore missing `edge_media_to_comment` fields on `instagram` ([#250](https://github.com/mikf/gallery-dl/issues/250))
- Fix serialization of `datetime` objects for `--write-metadata` ([#251](https://github.com/mikf/gallery-dl/issues/251), [#252](https://github.com/mikf/gallery-dl/issues/252))
- Allow multiple post-processor command-line options at once ([#253](https://github.com/mikf/gallery-dl/issues/253))
- Prevent crash on `booru` sites when no tags are available ([#259](https://github.com/mikf/gallery-dl/issues/259))
- Fix extraction on `instagram` after `rhx_gis` field removal ([#266](https://github.com/mikf/gallery-dl/issues/266))
- Avoid Cloudflare CAPTCHAs for Python interpreters built against OpenSSL < 1.1.1
- Miscellaneous fixes for `luscious`

## 1.8.3 - 2019-05-04
### Additions
- Support for
  - `plurk`  - https://www.plurk.com/ ([#212](https://github.com/mikf/gallery-dl/issues/212))
  - `sexcom` - https://www.sex.com/   ([#147](https://github.com/mikf/gallery-dl/issues/147))
- `--clear-cache`
- `date` metadata fields for `deviantart`, `twitter`, and `tumblr` ([#224](https://github.com/mikf/gallery-dl/issues/224), [#232](https://github.com/mikf/gallery-dl/issues/232))
### Changes
- Standalone executables are now built using PyInstaller:
  - uses the latest CPython interpreter (Python 3.7.3)
  - available on several platforms (Windows, Linux, macOS)
  - includes the `certifi` CA bundle, `youtube-dl`, and `pyOpenSSL` on Windows
### Fixes
- Patch `urllib3`'s  default list of SSL/TLS ciphers to prevent Cloudflare CAPTCHAs ([#227](https://github.com/mikf/gallery-dl/issues/227))
  (Windows users need to install `pyOpenSSL` for this to take effect)
- Provide fallback URLs for `twitter` images ([#237](https://github.com/mikf/gallery-dl/issues/237))
- Send `Referer` headers when downloading from `hitomi` ([#239](https://github.com/mikf/gallery-dl/issues/239))
- Updated login procedure on `mangoxo`

## 1.8.2 - 2019-04-12
### Additions
- Support for
  - `pixnet`   - https://www.pixnet.net/  ([#177](https://github.com/mikf/gallery-dl/issues/177))
  - `wikiart`  - https://www.wikiart.org/ ([#179](https://github.com/mikf/gallery-dl/issues/179))
  - `mangoxo`  - https://www.mangoxo.com/ ([#184](https://github.com/mikf/gallery-dl/issues/184))
  - `yaplog`   - https://yaplog.jp/       ([#190](https://github.com/mikf/gallery-dl/issues/190))
  - `livedoor` - http://blog.livedoor.jp/ ([#190](https://github.com/mikf/gallery-dl/issues/190))
- Login support for `mangoxo` ([#184](https://github.com/mikf/gallery-dl/issues/184)) and `twitter` ([#214](https://github.com/mikf/gallery-dl/issues/214))
### Changes
- Increased required `Requests` version to 2.11.0
### Fixes
- Improved image quality on `reactor` sites ([#210](https://github.com/mikf/gallery-dl/issues/210))
- Support `imagebam` galleries with more than 100 images ([#219](https://github.com/mikf/gallery-dl/issues/219))
- Updated Cloudflare bypass code

## 1.8.1 - 2019-03-29
### Additions
- Support for:
  - `35photo` - https://35photo.pro/ ([#162](https://github.com/mikf/gallery-dl/issues/162))
  - `500px`   - https://500px.com/   ([#185](https://github.com/mikf/gallery-dl/issues/185))
- `instagram` extractor for hashtags ([#202](https://github.com/mikf/gallery-dl/issues/202))
- Option to get more metadata on `deviantart` ([#189](https://github.com/mikf/gallery-dl/issues/189))
- Man pages and bash completion ([#150](https://github.com/mikf/gallery-dl/issues/150))
- Snap improvements ([#197](https://github.com/mikf/gallery-dl/issues/197), [#199](https://github.com/mikf/gallery-dl/issues/199), [#207](https://github.com/mikf/gallery-dl/issues/207))
### Changes
- Better FFmpeg arguments for `--ugoira-conv`
- Adjusted metadata for `luscious` albums
### Fixes
- Proper handling of `instagram` multi-image posts ([#178](https://github.com/mikf/gallery-dl/issues/178), [#201](https://github.com/mikf/gallery-dl/issues/201))
- Fixed `tumblr` avatar URLs when not using OAuth1.0 ([#193](https://github.com/mikf/gallery-dl/issues/193))
- Miscellaneous fixes for `exhentai`, `komikcast`

## 1.8.0 - 2019-03-15
### Additions
- Support for:
  - `weibo`       - https://www.weibo.com/
  - `pururin`     - https://pururin.io/          ([#174](https://github.com/mikf/gallery-dl/issues/174))
  - `fashionnova` - https://www.fashionnova.com/ ([#175](https://github.com/mikf/gallery-dl/issues/175))
  - `shopify` sites in general ([#175](https://github.com/mikf/gallery-dl/issues/175))
- Snap packaging ([#169](https://github.com/mikf/gallery-dl/issues/169), [#170](https://github.com/mikf/gallery-dl/issues/170), [#187](https://github.com/mikf/gallery-dl/issues/187), [#188](https://github.com/mikf/gallery-dl/issues/188))
- Automatic Cloudflare DDoS protection bypass
- Extractor and Job information for logging format strings
- `dynastyscans` image and search extractors ([#163](https://github.com/mikf/gallery-dl/issues/163))
- `deviantart` scraps extractor ([#168](https://github.com/mikf/gallery-dl/issues/168))
- `artstation` extractor for artwork listings ([#172](https://github.com/mikf/gallery-dl/issues/172))
- `smugmug` video support and improved image format selection ([#183](https://github.com/mikf/gallery-dl/issues/183))
### Changes
- More metadata for `nhentai` galleries
- Combined `myportfolio` extractors into one
- Renamed `name` metadata field to `filename` and removed the original `filename` field
- Simplified and improved internal data structures
- Optimized creation of child extractors
### Fixes
- Filter empty `tumblr` URLs ([#165](https://github.com/mikf/gallery-dl/issues/165))
- Filter ads and improve connection speed on `hentaifoundry`
- Show proper error messages if `luscious` galleries are unavailable
- Miscellaneous fixes for `mangahere`, `ngomik`, `simplyhentai`, `imgspice`
### Removals
- `seaotterscans`

## 1.7.0 - 2019-02-05
- Added support for:
  - `photobucket` - http://photobucket.com/ ([#117](https://github.com/mikf/gallery-dl/issues/117))
  - `hentaifox` - https://hentaifox.com/ ([#160](https://github.com/mikf/gallery-dl/issues/160))
  - `tsumino` - https://www.tsumino.com/ ([#161](https://github.com/mikf/gallery-dl/issues/161))
- Added the ability to dynamically generate extractors based on a user's config file for
  - [`mastodon`](https://github.com/tootsuite/mastodon) instances ([#144](https://github.com/mikf/gallery-dl/issues/144))
  - [`foolslide`](https://github.com/FoolCode/FoOlSlide) based sites
  - [`foolfuuka`](https://github.com/FoolCode/FoolFuuka) based archives
- Added an extractor for `behance` collections ([#157](https://github.com/mikf/gallery-dl/issues/157))
- Added login support for `luscious` ([#159](https://github.com/mikf/gallery-dl/issues/159)) and `tsumino` ([#161](https://github.com/mikf/gallery-dl/issues/161))
- Added an option to stop downloading if the `exhentai` image limit is exceeded ([#141](https://github.com/mikf/gallery-dl/issues/141))
- Fixed extraction issues for `behance` and `mangapark`

## 1.6.3 - 2019-01-18
- Added `metadata` post-processor to write image metadata to an external file ([#135](https://github.com/mikf/gallery-dl/issues/135))
- Added option to reverse chapter order of manga extractors ([#149](https://github.com/mikf/gallery-dl/issues/149))
- Added authentication support for `danbooru` ([#151](https://github.com/mikf/gallery-dl/issues/151))
- Added tag metadata for `exhentai` and `hbrowse` galleries
- Improved `*reactor` extractors ([#148](https://github.com/mikf/gallery-dl/issues/148))
- Fixed extraction issues for `nhentai` ([#156](https://github.com/mikf/gallery-dl/issues/156)), `pinterest`, `mangapark`

## 1.6.2 - 2019-01-01
- Added support for:
  - `instagram` - https://www.instagram.com/ ([#134](https://github.com/mikf/gallery-dl/issues/134))
- Added support for multiple items on sta.sh pages ([#113](https://github.com/mikf/gallery-dl/issues/113))
- Added option to download `tumblr` avatars ([#137](https://github.com/mikf/gallery-dl/issues/137))
- Changed defaults for visited post types and inline media on `tumblr`
- Improved inline extraction of `tumblr` posts ([#133](https://github.com/mikf/gallery-dl/issues/133), [#137](https://github.com/mikf/gallery-dl/issues/137))
- Improved error handling and retry behavior of all API calls
- Improved handling of missing fields in format strings ([#136](https://github.com/mikf/gallery-dl/issues/136))
- Fixed hash extraction for unusual `tumblr` URLs ([#129](https://github.com/mikf/gallery-dl/issues/129))
- Fixed image subdomains for `hitomi` galleries ([#142](https://github.com/mikf/gallery-dl/issues/142))
- Fixed and improved miscellaneous issues for `kissmanga` ([#20](https://github.com/mikf/gallery-dl/issues/20)), `luscious`, `mangapark`, `readcomiconline`

## 1.6.1 - 2018-11-28
- Added support for:
  - `joyreactor` - http://joyreactor.cc/ ([#114](https://github.com/mikf/gallery-dl/issues/114))
  - `pornreactor` - http://pornreactor.cc/ ([#114](https://github.com/mikf/gallery-dl/issues/114))
  - `newgrounds` - https://www.newgrounds.com/ ([#119](https://github.com/mikf/gallery-dl/issues/119))
- Added extractor for search results on `luscious` ([#127](https://github.com/mikf/gallery-dl/issues/127))
- Fixed filenames of ZIP archives ([#126](https://github.com/mikf/gallery-dl/issues/126))
- Fixed extraction issues for `gfycat`, `hentaifoundry` ([#125](https://github.com/mikf/gallery-dl/issues/125)), `mangafox`

## 1.6.0 - 2018-11-17
- Added support for:
  - `wallhaven` - https://alpha.wallhaven.cc/
  - `yuki` - https://yuki.la/
- Added youtube-dl integration and video downloads for `twitter` ([#99](https://github.com/mikf/gallery-dl/issues/99)), `behance`, `artstation`
- Added per-extractor options for network connections (`retries`, `timeout`, `verify`)
- Added a `--no-check-certificate` command-line option
- Added ability to specify the number of skipped downloads before aborting/exiting ([#115](https://github.com/mikf/gallery-dl/issues/115))
- Added extractors for scraps, favorites, popular and recent images on `hentaifoundry` ([#110](https://github.com/mikf/gallery-dl/issues/110))
- Improved login procedure for `pixiv`  to avoid unwanted emails on each new login
- Improved album metadata and error handling for `flickr` ([#109](https://github.com/mikf/gallery-dl/issues/109))
- Updated default User-Agent string to Firefox 62 ([#122](https://github.com/mikf/gallery-dl/issues/122))
- Fixed `twitter` API response handling when logged in ([#123](https://github.com/mikf/gallery-dl/issues/123))
- Fixed issue when converting Ugoira using H.264
- Fixed miscellaneous issues for `2chan`, `deviantart`, `fallenangels`, `flickr`, `imagefap`, `pinterest`, `turboimagehost`, `warosu`, `yuki` ([#112](https://github.com/mikf/gallery-dl/issues/112))

## 1.5.3 - 2018-09-14
- Added support for:
  - `hentaicafe` - https://hentai.cafe/ ([#101](https://github.com/mikf/gallery-dl/issues/101))
  - `bobx` - http://www.bobx.com/dark/
- Added black-/whitelist options for post-processor modules
- Added support for `tumblr` inline videos ([#102](https://github.com/mikf/gallery-dl/issues/102))
- Fixed extraction of `smugmug` albums without owner ([#100](https://github.com/mikf/gallery-dl/issues/100))
- Fixed issues when using default config values with `reddit` extractors ([#104](https://github.com/mikf/gallery-dl/issues/104))
- Fixed pagination for user favorites on `sankaku` ([#106](https://github.com/mikf/gallery-dl/issues/106))
- Fixed a crash when processing `deviantart` journals ([#108](https://github.com/mikf/gallery-dl/issues/108))

## 1.5.2 - 2018-08-31
- Added support for `twitter` timelines ([#96](https://github.com/mikf/gallery-dl/issues/96))
- Added option to suppress FFmpeg output during ugoira conversions
- Improved filename formatter performance
- Improved inline image quality on `tumblr` ([#98](https://github.com/mikf/gallery-dl/issues/98))
- Fixed image URLs for newly released `mangadex` chapters
- Fixed a smaller issue with `deviantart` journals
- Replaced `subapics` with `ngomik`

## 1.5.1 - 2018-08-17
- Added support for:
  - `piczel` - https://piczel.tv/
- Added support for related pins on `pinterest`
- Fixed accessing "offensive" galleries on `exhentai` ([#97](https://github.com/mikf/gallery-dl/issues/97))
- Fixed extraction issues for `mangadex`, `komikcast` and `behance`
- Removed original-image functionality from `tumblr`, since "raw" images are no longer accessible

## 1.5.0 - 2018-08-03
- Added support for:
  - `behance` - https://www.behance.net/
  - `myportfolio` - https://www.myportfolio.com/ ([#95](https://github.com/mikf/gallery-dl/issues/95))
- Added custom format string options to handle long strings ([#92](https://github.com/mikf/gallery-dl/issues/92), [#94](https://github.com/mikf/gallery-dl/issues/94))
  - Slicing: `"{field[10:40]}"`
  - Replacement: `"{field:L40/too long/}"`
- Improved frame rate handling for ugoira conversions
- Improved private access token usage on `deviantart`
- Fixed metadata extraction for some images on `nijie`
- Fixed chapter extraction on `mangahere`
- Removed `whatisthisimnotgoodwithcomputers`
- Removed support for Python 3.3

## 1.4.2 - 2018-07-06
- Added image-pool extractors for `safebooru` and `rule34`
- Added option for extended tag information on `booru` sites ([#92](https://github.com/mikf/gallery-dl/issues/92))
- Added support for DeviantArt's new URL format
- Added support for `mangapark` mirrors
- Changed `imagefap` extractors to use HTTPS
- Fixed crash when skipping downloads for files without known extension

## 1.4.1 - 2018-06-22
- Added an `ugoira` post-processor to convert  `pixiv` animations to WebM
- Added `--zip` and `--ugoira-conv` command-line options
- Changed how ugoira frame information is handled
  - instead of being written to a separate file, it is now made available as metadata field of the ZIP archive
- Fixed manga and chapter titles for `mangadex`
- Fixed file deletion by post-processors

## 1.4.0 - 2018-06-08
- Added support for:
  - `simplyhentai` - https://www.simply-hentai.com/ ([#89](https://github.com/mikf/gallery-dl/issues/89))
- Added extractors for
  - `pixiv` search results and followed users
  - `deviantart` search results and popular listings
- Added post-processors to perform actions on downloaded files
- Added options to configure logging behavior
- Added OAuth support for `smugmug`
- Changed `pixiv` extractors to use the AppAPI
  - this breaks `favorite` archive IDs and changes some metadata fields
- Changed the default filename format for `tumblr` and renamed `offset` to `num`
- Fixed a possible UnicodeDecodeError during installation ([#86](https://github.com/mikf/gallery-dl/issues/86))
- Fixed extraction of `mangadex` manga with more than 100 chapters ([#84](https://github.com/mikf/gallery-dl/issues/84))
- Fixed miscellaneous issues for `imgur`, `reddit`, `komikcast`, `mangafox` and `imagebam`

## 1.3.5 - 2018-05-04
- Added support for:
  - `smugmug` - https://www.smugmug.com/
- Added title information for `mangadex` chapters
- Improved the `pinterest` API implementation ([#83](https://github.com/mikf/gallery-dl/issues/83))
- Improved error handling for `deviantart` and `tumblr`
- Removed `gomanga` and `puremashiro`

## 1.3.4 - 2018-04-20
- Added support for custom OAuth2 credentials for `pinterest`
- Improved rate limit handling for `tumblr` extractors
- Improved `hentaifoundry` extractors
- Improved `imgur` URL patterns
- Fixed miscellaneous extraction issues for `luscious` and `komikcast`
- Removed `loveisover` and `spectrumnexus`

## 1.3.3 - 2018-04-06
- Added extractors for
  - `nhentai` search results
  - `exhentai` search results and favorites
  - `nijie` doujins and favorites
- Improved metadata extraction for `exhentai` and `nijie`
- Improved `tumblr` extractors by avoiding unnecessary API calls
- Fixed Cloudflare DDoS protection bypass
- Fixed errors when trying to print unencodable characters

## 1.3.2 - 2018-03-23
- Added extractors for `artstation` albums, challenges and search results
- Improved URL and metadata extraction for `hitomi`and `nhentai`
- Fixed page transitions for `danbooru` API results ([#82](https://github.com/mikf/gallery-dl/issues/82))

## 1.3.1 - 2018-03-16
- Added support for:
  - `mangadex` - https://mangadex.org/
  - `artstation` - https://www.artstation.com/
- Added Cloudflare DDoS protection bypass to `komikcast` extractors
- Changed archive ID formats for `deviantart` folders and collections
- Improved error handling for `deviantart` API calls
- Removed `imgchili` and various smaller image hosts

## 1.3.0 - 2018-03-02
- Added `--proxy` to explicitly specify a proxy server ([#76](https://github.com/mikf/gallery-dl/issues/76))
- Added options to customize [archive ID formats](https://github.com/mikf/gallery-dl/blob/master/docs/configuration.rst#extractorarchive-format) and [undefined replacement fields](https://github.com/mikf/gallery-dl/blob/master/docs/configuration.rst#extractorkeywords-default)
- Changed various archive ID formats to improve their behavior for favorites / bookmarks / etc.
  - Affected modules are `deviantart`, `flickr`, `tumblr`, `pixiv` and all …boorus
- Improved `sankaku` and `idolcomplex` support by
  - respecting `page` and `next` URL parameters ([#79](https://github.com/mikf/gallery-dl/issues/79))
  - bypassing the page-limit for unauthenticated users
- Improved `directlink` metadata by properly unquoting it
- Fixed `pixiv` ugoira extraction ([#78](https://github.com/mikf/gallery-dl/issues/78))
- Fixed miscellaneous extraction issues for `mangastream` and `tumblr`
- Removed `yeet`, `chronos`, `coreimg`, `hosturimage`, `imageontime`, `img4ever`, `imgmaid`, `imgupload`

## 1.2.0 - 2018-02-16
- Added support for:
  - `paheal` - https://rule34.paheal.net/ ([#69](https://github.com/mikf/gallery-dl/issues/69))
  - `komikcast` - https://komikcast.com/ ([#70](https://github.com/mikf/gallery-dl/issues/70))
  - `subapics` - http://subapics.com/ ([#70](https://github.com/mikf/gallery-dl/issues/70))
- Added `--download-archive` to record downloaded files in an archive file
- Added `--write-log` to write logging output to a file
- Added a filetype check on download completion to fix incorrectly assigned filename extensions ([#63](https://github.com/mikf/gallery-dl/issues/63))
- Added the `tumblr:...` pseudo URI scheme to support custom domains for Tumblr blogs ([#71](https://github.com/mikf/gallery-dl/issues/71))
- Added fallback URLs for `tumblr` images ([#64](https://github.com/mikf/gallery-dl/issues/64))
- Added support for `reddit`-hosted images ([#68](https://github.com/mikf/gallery-dl/issues/68))
- Improved the input file format by allowing comments and per-URL options
- Fixed OAuth 1.0 signature generation for Python 3.3 and 3.4 ([#75](https://github.com/mikf/gallery-dl/issues/75))
- Fixed smaller issues for `luscious`, `hentai2read`, `hentaihere` and `imgur`
- Removed the `batoto` module

## 1.1.2 - 2018-01-12
- Added support for:
  - `puremashiro` - http://reader.puremashiro.moe/ ([#66](https://github.com/mikf/gallery-dl/issues/66))
  - `idolcomplex` - https://idol.sankakucomplex.com/
- Added an option to filter reblogs on `tumblr` ([#61](https://github.com/mikf/gallery-dl/issues/61))
- Added OAuth user authentication for `tumblr` ([#65](https://github.com/mikf/gallery-dl/issues/65))
- Added support for `slideshare` mobile URLs ([#67](https://github.com/mikf/gallery-dl/issues/67))
- Improved pagination for various …booru sites to work around page limits
- Fixed chapter information parsing for certain manga on `kissmanga` ([#58](https://github.com/mikf/gallery-dl/issues/58)) and `batoto` ([#60](https://github.com/mikf/gallery-dl/issues/60))

## 1.1.1 - 2017-12-22
- Added support for:
  - `slideshare` - https://www.slideshare.net/ ([#54](https://github.com/mikf/gallery-dl/issues/54))
- Added pool- and post-extractors for `sankaku`
- Added OAuth user authentication for `deviantart`
- Updated `luscious` to support `members.luscious.net` URLs ([#55](https://github.com/mikf/gallery-dl/issues/55))
- Updated `mangahere` to use their new domain name (mangahere.cc) and support mobile URLs
- Updated `gelbooru` to not be restricted to the first 20,000 images ([#56](https://github.com/mikf/gallery-dl/issues/56))
- Fixed extraction issues for `nhentai` and `khinsider`

## 1.1.0 - 2017-12-08
- Added the ``-r/--limit-rate`` command-line option to set a maximum download rate
- Added the ``--sleep`` command-line option to specify the number of seconds to sleep before each download
- Updated `gelbooru` to no longer use their now disabled API
- Fixed SWF extraction for `sankaku` ([#52](https://github.com/mikf/gallery-dl/issues/52))
- Fixed extraction issues for `hentai2read` and `khinsider`
- Removed the deprecated `--images` and `--chapters` options
- Removed the ``mangazuki`` module

## 1.0.2 - 2017-11-24
- Added an option to set a [custom user-agent string](https://github.com/mikf/gallery-dl/blob/master/docs/configuration.rst#extractoruser-agent)
- Improved retry behavior for failed HTTP requests
- Improved `seiga` by providing better metadata and getting more than the latest 200 images
- Improved `tumblr` by adding support for [all post types](https://github.com/mikf/gallery-dl/blob/master/docs/configuration.rst#extractortumblrposts), scanning for [inline images](https://github.com/mikf/gallery-dl/blob/master/docs/configuration.rst#extractortumblrinline) and following [external links](https://github.com/mikf/gallery-dl/blob/master/docs/configuration.rst#extractortumblrexternal) ([#48](https://github.com/mikf/gallery-dl/issues/48))
- Fixed extraction issues for `hbrowse`, `khinsider` and `senmanga`

## 1.0.1 - 2017-11-10
- Added support for:
  - `xvideos` - https://www.xvideos.com/ ([#45](https://github.com/mikf/gallery-dl/issues/45))
- Fixed exception handling during file downloads which could lead to a premature exit
- Fixed an issue with `tumblr` where not all images would be downloaded when using tags ([#48](https://github.com/mikf/gallery-dl/issues/48))
- Fixed extraction issues for `imgbox` ([#47](https://github.com/mikf/gallery-dl/issues/47)), `mangastream` ([#49](https://github.com/mikf/gallery-dl/issues/49)) and `mangahere`

## 1.0.0 - 2017-10-27
- Added support for:
  - `warosu` - https://warosu.org/
  - `b4k` - https://arch.b4k.co/
- Added support for `pixiv` ranking lists
- Added support for `booru` popular lists (`danbooru`, `e621`, `konachan`, `yandere`, `3dbooru`)
- Added the `--cookies` command-line and [`cookies`](https://github.com/mikf/gallery-dl/blob/master/docs/configuration.rst#extractorcookies) config option to load additional cookies
- Added the `--filter` and `--chapter-filter` command-line options to select individual images or manga-chapters by their metadata using simple Python expressions ([#43](https://github.com/mikf/gallery-dl/issues/43))
- Added the [`verify`](https://github.com/mikf/gallery-dl/blob/master/docs/configuration.rst#downloaderhttpverify) config option to control certificate verification during file downloads
- Added config options to overwrite internally used API credentials ([API Tokens & IDs](https://github.com/mikf/gallery-dl/blob/master/docs/configuration.rst#api-tokens-ids))
- Added `-K` as a shortcut for `--list-keywords`
- Changed the `--images` and `--chapters` command-line options to `--range` and `--chapter-range`
- Changed keyword names for various modules to make them accessible by `--filter`. In general minus signs have been replaced with underscores (e.g. `gallery-id`  -> `gallery_id`).
- Changed default filename formats for manga extractors to optionally use volume and title information
- Improved the downloader modules to use [`.part` files](https://github.com/mikf/gallery-dl/blob/master/docs/configuration.rst#downloaderpart) and support resuming incomplete downloads ([#29](https://github.com/mikf/gallery-dl/issues/29))
- Improved `deviantart` by distinguishing between users and groups ([#26](https://github.com/mikf/gallery-dl/issues/26)), always using HTTPS, and always downloading full-sized original images
- Improved `sankaku` by adding authentication support and fixing various other issues ([#44](https://github.com/mikf/gallery-dl/issues/44))
- Improved URL pattern for direct image links ([#30](https://github.com/mikf/gallery-dl/issues/30))
- Fixed an issue with `luscious` not getting original image URLs ([#33](https://github.com/mikf/gallery-dl/issues/33))
- Fixed various smaller issues for `batoto`, `hentai2read` ([#38](https://github.com/mikf/gallery-dl/issues/38)), `jaiminisbox`, `khinsider`, `kissmanga` ([#28](https://github.com/mikf/gallery-dl/issues/28), [#46](https://github.com/mikf/gallery-dl/issues/46)), `mangahere`, `pawoo`, `twitter`
- Removed `kisscomic` and `yonkouprod` modules

## 0.9.1 - 2017-07-24
- Added support for:
  - `2chan` - https://www.2chan.net/
  - `4plebs` - https://archive.4plebs.org/
  - `archivedmoe` - https://archived.moe/
  - `archiveofsins` - https://archiveofsins.com/
  - `desuarchive` - https://desuarchive.org/
  - `fireden` - https://boards.fireden.net/
  - `loveisover` - https://archive.loveisover.me/
  - `nyafuu` - https://archive.nyafuu.org/
  - `rbt` - https://rbt.asia/
  - `thebarchive` - https://thebarchive.com/
  - `mangazuki` - https://mangazuki.co/
- Improved `reddit` to allow submission filtering by ID and human-readable dates
- Improved `deviantart` to support group galleries and gallery folders ([#26](https://github.com/mikf/gallery-dl/issues/26))
- Changed `deviantart` to use better default path formats
- Fixed extraction of larger `imgur` albums
- Fixed some smaller issues for `pixiv`, `batoto` and `fallenangels`

## 0.9.0 - 2017-06-28
- Added support for:
  - `reddit` - https://www.reddit.com/ ([#15](https://github.com/mikf/gallery-dl/issues/15))
  - `flickr` - https://www.flickr.com/ ([#16](https://github.com/mikf/gallery-dl/issues/16))
  - `gfycat` - https://gfycat.com/
- Added support for direct image links
- Added user authentication via [OAuth](https://github.com/mikf/gallery-dl#52oauth) for `reddit` and `flickr`
- Added support for user authentication data from [`.netrc`](https://stackoverflow.com/tags/.netrc/info) files ([#22](https://github.com/mikf/gallery-dl/issues/22))
- Added a simple progress indicator for multiple URLs ([#19](https://github.com/mikf/gallery-dl/issues/19))
- Added the `--write-unsupported` command-line option to write unsupported URLs to a file
- Added documentation for all available config options ([configuration.rst](https://github.com/mikf/gallery-dl/blob/master/docs/configuration.rst))
- Improved `pixiv` to support tags for user downloads ([#17](https://github.com/mikf/gallery-dl/issues/17))
- Improved `pixiv` to support shortened and http://pixiv.me/... URLs ([#23](https://github.com/mikf/gallery-dl/issues/23))
- Improved `imgur` to properly handle `.gifv` images and provide better metadata
- Fixed an issue with `kissmanga` where metadata parsing for some series failed ([#20](https://github.com/mikf/gallery-dl/issues/20))
- Fixed an issue with getting filename extensions from `Content-Type` response headers

## 0.8.4 - 2017-05-21
- Added the `--abort-on-skip` option to stop extraction if a download would be skipped
- Improved the output format of the `--list-keywords` option
- Updated `deviantart` to support all media types and journals
- Updated `fallenangels` to support their [Vietnamese version](https://truyen.fascans.com/)
- Fixed an issue with multiple tags on ...booru sites
- Removed the `yomanga` module

## 0.8.3 - 2017-05-01
- Added support for https://pawoo.net/
- Added manga extractors for all [FoOlSlide](https://foolcode.github.io/FoOlSlide/)-based modules
- Added the `-q/--quiet` and `-v/--verbose` options to control output verbosity
- Added the `-j/--dump-json` option to dump extractor results in JSON format
- Added the `--ignore-config` option
- Updated the `exhentai` extractor to fall back to using the e-hentai version if no username is given
- Updated `deviantart` to support sta.sh URLs
- Fixed an issue with `kissmanga` which prevented image URLs from being decrypted properly (again)
- Fixed an issue with `pixhost` where for an image inside an album it would always download the first image of that album ([#13](https://github.com/mikf/gallery-dl/issues/13))
- Removed the `mangashare` and `readcomics` modules

## 0.8.2 - 2017-04-10
- Fixed an issue in `kissmanga` which prevented image URLs from being decrypted properly

## 0.8.1 - 2017-04-09
- Added new extractors:
  - `kireicake` - https://reader.kireicake.com/
  - `seaotterscans` - https://reader.seaotterscans.com/
- Added a favourites extractor for `deviantart`
- Re-enabled the `kissmanga` module
- Updated `nijie` to support multi-page image listings
- Updated `mangastream` to support readms.net URLs
- Updated `exhentai` to support e-hentai.org URLs
- Updated `fallenangels` to support their new domain and site layout

## 0.8.0 - 2017-03-28
- Added logging support
- Added the `-R/--retries` option to specify how often a download should be retried before giving up
- Added the `--http-timeout` option to set a timeout for HTTP connections
- Improved error handling/tolerance during HTTP file downloads ([#10](https://github.com/mikf/gallery-dl/issues/10))
- Improved option parsing and the help message from `-h/--help`
- Changed the way configuration values are used by prioritizing top-level values
  - This allows for cmdline options like `-u/--username` to overwrite values set in configuration files
- Fixed an issue with `imagefap.com` where incorrectly reported gallery sizes would cause the extractor to fail ([#9](https://github.com/mikf/gallery-dl/issues/9))
- Fixed an issue with `seiga.nicovideo.jp` where invalid characters in an API response caused the XML parser to fail
- Fixed an issue with `seiga.nicovideo.jp` where the filename extension for the first image would be used for all others
- Removed support for old configuration paths on Windows
- Removed several modules:
  - `mangamint`: site is down
  - `whentai`: now requires account with VIP status for original images
  - `kissmanga`: encrypted image URLs (will be re-added later)

## 0.7.0 - 2017-03-06
- Added `--images` and `--chapters` options
  - Specifies which images (or chapters) to download through a comma-separated list of indices or index-ranges
  - Example: `--images -2,4,6-8,10-` will select images with index 1, 2, 4, 6, 7, 8 and 10 up to the last one
- Changed the `-g`/`--get-urls` option
  - The amount of how often the -g option is given now determines up until which level URLs are resolved.
  - See 3bca86618505c21628cd9c7179ce933a78d00ca2
- Changed several option keys:
  - `directory_fmt` -> `directory`
  - `filename_fmt` -> `filename`
  - `download-original` -> `original`
- Improved [FoOlSlide](https://foolcode.github.io/FoOlSlide/)-based extractors
- Fixed URL extraction for hentai2read
- Fixed an issue with deviantart, where the API access token wouldn't get refreshed

## 0.6.4 - 2017-02-13
- Added new extractors:
  - fallenangels (famatg.com)
- Fixed url- and data-extraction for:
  - nhentai
  - mangamint
  - twitter
  - imagetwist
- Disabled InsecureConnectionWarning when no certificates are available

## 0.6.3 - 2017-01-25
- Added new extractors:
  - gomanga
  - yomanga
  - mangafox
- Fixed deviantart extractor failing - switched to using their API
- Fixed an issue with SQLite on Python 3.6
- Automated test builds via Travis CI
- Standalone executables for Windows

## 0.6.2 - 2017-01-05
- Added new extractors:
  - kisscomic
  - readcomics
  - yonkouprod
  - jaiminisbox
- Added manga extractor to batoto-module
- Added user extractor to seiga-module
- Added `-i`/`--input-file` argument to allow local files and stdin as input (like wget)
- Added basic support for `file://` URLs
  - this allows for the recursive extractor to be applied to local files:
  - `$ gallery-dl r:file://[path to file]`
- Added a utility extractor to run unit test URLs
- Updated luscious to deal with API changes
- Fixed twitter to provide the original image URL
- Minor fixes to hentaifoundry
- Removed imgclick extractor

## 0.6.1 - 2016-11-30
- Added new extractors:
  - whentai
  - readcomiconline
  - sensescans, worldthree
  - imgmaid, imagevenue, img4ever, imgspot, imgtrial, pixhost
- Added base class for extractors of [FoOlSlide](https://foolcode.github.io/FoOlSlide/)-based sites
- Changed default paths for configuration files on Windows
  - old paths are still supported, but that will change in future versions
- Fixed aborting downloads if a single one failed ([#5](https://github.com/mikf/gallery-dl/issues/5))
- Fixed cloudflare-bypass cache containing outdated cookies
- Fixed image URLs for hitomi and 8chan
- Updated deviantart to always provide the highest quality image
- Updated README.rst
- Removed doujinmode extractor

## 0.6.0 - 2016-10-08
- Added new extractors:
  - hentaihere
  - dokireader
  - twitter
  - rapidimg, picmaniac
- Added support to find filename extensions by Content-Type response header
- Fixed filename/path issues on Windows ([#4](https://github.com/mikf/gallery-dl/issues/4)):
  - Enable path names with more than 260 characters
  - Remove trailing spaces in path segments
- Updated Job class to automatically set category/subcategory keywords

## 0.5.2 - 2016-09-23
- Added new extractors:
  - pinterest
  - rule34
  - dynastyscans
  - imagebam, coreimg, imgcandy, imgtrex
- Added login capabilities for batoto
- Added `--version` cmdline argument to print the current program version and exit
- Added `--list-extractors` cmdline argument to print names of all extractor classes together with descriptions and example URLs
- Added proper error messages if an image/user does not exist
- Added unittests for every extractor

## 0.5.1 - 2016-08-22
- Added new extractors:
  - luscious
  - doujinmode
  - hentaibox
  - seiga
  - imagefap
- Changed error output to use stderr instead of stdout
- Fixed broken pipes causing an exception-dump by catching BrokenPipeErrors

## 0.5.0 - 2016-07-25

## 0.4.1 - 2015-12-03
- New modules (imagetwist, turboimagehost)
- Manga-extractors: Download entire manga and not just single chapters
- Generic extractor (provisional)
- Better and configurable console output
- Windows support

## 0.4.0 - 2015-11-26

## 0.3.3 - 2015-11-10

## 0.3.2 - 2015-11-04

## 0.3.1 - 2015-10-30

## 0.3.0 - 2015-10-05

## 0.2.0 - 2015-06-28

## 0.1.0 - 2015-05-27
