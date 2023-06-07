#!/usr/bin/env python3
import base64
from sys import stdin
from typing import Any

from google.protobuf.message import DecodeError, Message

from proto.ved_pb2 import Ved

"""
    The type of link encoded in the ved message. If you find out, what other values mean,
    please either send me a pull request or comment in the article
    (http://gqs-decoder.blogspot.com/2013/08/google-referrer-query-strings-debunked-part-1.html)
"""
LINK_TYPES = {
    22: "web",
    152: "blog search result",
    232: "book search result",
    232: "patent result",
    235: "book search result thumbnail",
    235: "patent result thumbnail",
    244: "image result in standard SERPs",
    245: "image search result in basic (non-javascript) image search, or image result in universal search",
    288: "local search result",
    295: "news result thumbnail",
    297: "news result",
    300: "more results link (listed mainly for Q&A websites)",
    311: "video result",
    312: "video result thumbnail",
    338: "one-line sitelink",
    371: "shopping search result",
    429: "image search result [probably not in use any more]",
    586: '"Jump to" link',
    612: "map search result website link",
    646: "map search result thumbnail",
    706: "adword sitelink",
    745: "breadcrumb",
    1107: 'patent result "Overview" / "Related" / "Discuss" link',
    1140: "book search result author link",
    1146: "normal result thumbnail (e.g. for an application, recipe, etc.)",
    1150: "normal result thumbnail (e.g. for an application, recipe, etc.)",
    1455: "local search result marker pin icon",
    1532: "news sub-result (i.e. the same story from a different site)",
    1617: "adword (i.e. sponsored search result)",
    1701: "map search result",
    1732: "knowledge graph repeated sub-link (e.g. football team squad players, album track listings)",
    1907: "sponsored shopping result thumbnail (in right-hand column of universal search results)",
    1908: "sponsored shopping result (in right-hand column of universal search results)",
    1986: "sponsored shopping result thumbnail (in main column of universal search results)",
    1987: "sponsored shopping result (in main column of universal search results)",
    2060: "sitelink",
    2237: "news result video thumbnail",
    2459: "knowledge graph link",
    2847: 'authorship "by [author]" link',
    2937: "authorship thumbnail link",
    3588: "image search result (thumbnail)",
    3596: 'image search result preview "View image" link',
    3597: "image search result preview thumbnail",
    3598: "image search result preview title link",
    3599: 'image search result preview "Visit page" link',
    3724: "image search result preview grey website link underneath title",
    3836: "knowledge graph main image",
    5077: "in-depth article result",
    5078: "in-depth article result thumbnail",
    5158: "adword one-line sitelink",
    5497: "dictionary definition link",
}


def try_decode(s: str) -> bytes | None:
    """try to base64 decode s. return None, if decoding fails"""
    try:
        return base64.b64decode(s.encode("utf8") + b"=====", b"_-")
    except TypeError:
        return None


def decode_ved_plain(s: str) -> dict[str, int]:
    """decode the plain text varian of the ved parameter. no error checking."""

    key_mapping = {
        "i": "index_boost",
        "t": "type",
        "r": "result_position",
        "s": "start",
    }

    kv_pairs = s.split(",")
    kv_pairs = [x.split(":") for x in kv_pairs]
    return {key_mapping.get(k, k): int(v) for k, v in kv_pairs}


def dict_from_proto(message: Message) -> dict[str, Any]:
    ret = {}
    for k, v in message.ListFields():
        if k.type == k.TYPE_MESSAGE:
            ret[k.name] = dict_from_proto(v)
        else:
            ret[k.name] = v

    return ret


def decode_ved_protobuf(s: str) -> dict[str, Any] | None:
    """decode the protobuf variant of the ved parameter."""

    decoded = try_decode(s)
    if not decoded:
        return None
    ved = Ved()
    try:
        ved.ParseFromString(decoded)
        return dict_from_proto(ved)
    except DecodeError:
        return None


def decode_ved(s: str) -> dict[str, Any] | None:
    """decode a ved"""
    if not s:
        return None
    elif s.startswith("2"):
        return decode_ved_protobuf(s[1:])
    elif s.startswith("1"):
        return decode_ved_plain(s[1:])
    elif s.startswith("0"):
        return decode_ved_protobuf(s[1:])


def format_type(type: int) -> str:
    type_name = LINK_TYPES.get(type, "unknown")
    return f"{type_name} ({type})"


def format_ved(ved: dict[str, Any] | None) -> dict[str, Any] | None:
    if ved:
        if "type" in ved:
            ved["type"] = format_type(ved["type"])
        if "link_type" in ved:
            ved["link_type"] = format_type(ved["link_type"])

    return ved


def main():
    for line in stdin:
        line = line.strip()
        if not line:
            continue
        print(line, format_ved(decode_ved(line)))


if __name__ == "__main__":
    main()
