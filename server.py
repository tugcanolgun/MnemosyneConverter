"""This is an attempt to convert annotatorjs type to
W3C Annotation format in order for compliance"""
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
# Import W3C schemas
from resources.search import SearchService
from resources.to_w3c import to_w3c

app = Flask(__name__)
# cors = CORS(app, resources={r"/*": {"origins": "*"}})
CORS(app, origins="*")
api = Api(app)

# Main W3C API
URL = "http://annotationserver.xtptzahyma.us-east-1.elasticbeanstalk.com/"
# Endpoint for target.id
URL_FIND = "annotations/find?id="
# Endpoint for annotation creation
URL_CRT = "annotations"

class Search(Resource):
    """Annotator /search endpoint"""
    def get(self):
        response = SearchService(URL+URL_FIND).get()
        print(f"Returning {response['total']} annotations")
        return jsonify(response)


class Custom(Resource):
    """Main handler of the W3C objects"""
    def post(self, src:str) -> dict:
        data = request.get_json()
        print(data, src)
        pass

class Annotations(Resource):
    """Annotator create endpoint"""
    def post(self) -> None:
        """This endpoint will not be used for this project as
        the sent object does not have the URI of the annotated
        object"""
        # data = request.get_json(force=True)
        # print(data)
        return None


class AnnotationsEmpty(Resource):
    """Not required for this project"""
    def get(self, id:str) -> None:
        return None

    def delete(self, id:str) -> None:
        return None
    
    def put(self, id:str) -> None:
        return None

api.add_resource(Search, '/search')
api.add_resource(Custom, '/create/<path:src>')
api.add_resource(Annotations, '/annotations')
api.add_resource(AnnotationsEmpty, '/annotations/<string:id>')

if __name__ == '__main__':
    app.run(port=5100, debug=False, use_reloader=True)