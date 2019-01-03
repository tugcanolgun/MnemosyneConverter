import json
import requests
from resources.annotatorjs import annotatorjs


class SearchService:
    """Gets W3C formatted annotations and
    turns them into annotatorjs format"""
    def __init__(self, url: str) -> None:
        self.url: str = url
        self.counter: int = 1

    def validation(self, data: dict) -> bool:
        """A very primitive validator for checking the W3C
        object type as not all of the types are not supported"""
        if "type" not in data:
            print('Validation 1 failed')
            return False
        if "target" not in data or "body" not in data:
            print('Validation 2 failed')
            return False
        if data["target"]["type"] != "TextQuoteSelector" or "refinedBy" not in data["target"]:
            print('Validation 3 failed')
            return False
        if data["body"]["type"] != "TextualBody":
            print('Validation 4 failed')
            return False
        return True

    def objectify(self, data: dict) -> dict:
        """Tries to get data from W3C object and
        bind it to annotatorjs object type"""
        try:
            text: str = data["body"]["value"]
            quote: str = data["target"]["exact"]
            start: str = data["target"]["refinedBy"]["start"]
            end: str = data["target"]["refinedBy"]["end"]
            startOffset: int = data["target"]["prefix"]
            endOffset: int = data["target"]["suffix"]
        except Exception as ex:
            print("There was an error converting the object:", ex)
            return {}
        else:
            obj: dict = annotatorjs(quote, text, start, end, startOffset, endOffset)
            obj["id"] = self.counter
            self.counter += 1
            return obj

    def get(self):
        """Main function of the class
        Gets data from an API and tries to fill the
        annotatorjs type object with 'total' and 'rows'
        """
        data = requests.get(self.url)
        annotatations: list = json.loads(data.text)
        data: dict = {"total": 0, "rows": []}
        for anno in annotatations:
            if self.validation(anno):
                obj = self.objectify(anno)
                if obj:
                    # If the object is successfuly translated
                    data["rows"].append(obj)
        data["total"] = len(data["rows"])
        return data
