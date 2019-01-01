
def text():
    """Returns text equivalent of the W3C text"""
    return {
        "@context": "http://www.w3.org/ns/anno.jsonld",
        "type": "Annotation",
        "body": {
            "creator": "user",
            "type": "TextualBody",
            "value": "string"
        },
        "generator": {
            "homepage": "http://mnemosyne.ml",
            "id": "string",
            "name": "string",
            "type": "string"
        },
        "target": {
                "id": "string",
                "type": "TextQuoteSelector",
                "exact": "string",
                "format": "string",
                "source": "string",
                "prefix": 0,
                "suffix": 0,
                "refinedBy": {
                    "type": "TextPositionSelector",
                    "start": "/div[2]",
                    "end": "/div[2]"
                },
            },
        }
