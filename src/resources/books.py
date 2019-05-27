from flask_restplus import Resource
from ..server.instance import server


api = server.api
books = api.namespace("books", description="books", path="/api/v1/")


@books.route("/books")
class Books(Resource):
    def get(self):
        return "test"
