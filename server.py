"""This is an attempt to convert annotatorjs type to
W3C Annotation format in order for compliance"""
from flask import Flask, request, jsonify, render_template
from flask_restful import Resource, Api
from flask_cors import CORS
# Import W3C schemas
from resources.search import SearchService
from resources.to_w3c import from_ann

app = Flask(__name__)
# cors = CORS(app, resources={r"/*": {"origins": "*"}})
CORS(app, origins="*")
api = Api(app)

# Main W3C API
URL = "http://annotationserver.xtptzahyma.us-east-1.elasticbeanstalk.com/"
# Endpoint for target.id
URL_FIND = "annotations/generator?id="
# Endpoint for annotation creation
URL_CRT = "annotations"


class Search(Resource):
    """Annotator /search endpoint"""
    def get(self):
        response = SearchService(URL + URL_CRT).get()
        print(f"Returning {response['total']} annotations")
        return jsonify(response)


class Custom(Resource):
    """Main handler of the W3C objects"""
    def post(self, username: str, src: str) -> dict:
        data = request.get_json()
        from_ann(data, username, src, URL + URL_CRT)
        pass
        return jsonify(data)


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
    def get(self, id: str) -> None:
        return jsonify()

    def delete(self, id: str) -> None:
        return jsonify()

    def put(self, id: str) -> None:
        return jsonify()


@app.route('/')
def index():
    return render_template('index.html')

api.add_resource(Search, '/search')
api.add_resource(Custom, '/create/<string:username>/<path:src>')
api.add_resource(Annotations, '/annotations')
api.add_resource(AnnotationsEmpty, '/annotations/<string:id>')

if __name__ == '__main__':
    app.run(port=5100, debug=False, use_reloader=True)
