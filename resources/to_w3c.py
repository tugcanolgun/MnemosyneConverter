import json
import requests
from resources.w3c_schema import text as w3ctext
from delete import MOCK


def to_w3c(src: str,
           quote: str,
           prefix: str,
           suffix: str,
           start: str,
           end: str,
           text: str,
           user: str = "blue"
           ) -> dict:
    """Converts received object to w3c type"""
    ann: dict = w3ctext()
    ann["generator"]["id"] = src
    ann["body"]["user"] = user
    ann["body"]["value"] = text
    ann["target"]["id"] = src
    ann["target"]["exact"] = quote
    ann["target"]["prefix"] = prefix
    ann["target"]["suffix"] = suffix
    ann["target"]["refinedBy"]["start"] = start
    ann["target"]["refinedBy"]["end"] = end

    return ann


def from_ann(data: dict, src: str) -> dict:
    """Takes annotatorjs object and divides"""
    if "quote" not in data or "text" not in data or "ranges" not in data:
        return {}
    res: dict = to_w3c(src,
                       data["quote"],
                       data["ranges"][0]["startOffset"],
                       data["ranges"][0]["endOffset"],
                       data["ranges"][0]["start"],
                       data["ranges"][0]["end"],
                       data["text"],
                    )
    MOCK.append(res)
    headers = {'Content-type': 'application/ld+json'}
    req = requests.post("http://annotationserver.xtptzahyma.us-east-1.elasticbeanstalk.com/annotations",
        data=json.dumps(res),
        headers=headers)
    print(req.text)
    return res
