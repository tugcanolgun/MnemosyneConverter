
def annotatorjs(quote:str, text:str, start: str, end: str, startOffset:int, endOffset:int) -> dict:
    """Returns annotatorjs type object"""
    return {
        "id": 0,
        "quote": quote,
        "ranges": [
            {
            "start": start,
            "startOffset": startOffset,
            "end": end,
            "endOffset": endOffset
            }
        ],
        "text": text,
    }
