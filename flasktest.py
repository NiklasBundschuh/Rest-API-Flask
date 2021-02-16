from flask import Flask
from flask.globals import request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'about': 'Hello World!'}

class Multi(Resource):
    def get(self, num):
        return{'result' : num*10}

api.add_resource(HelloWorld, '/')
api.add_resource(Multi, '/multi/<int:num>')


if __name__ == '__main__':
    app.run(port=1337, debug=True)




