from flask import Flask
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)
parser = api.parser()
parser.add_argument('apiKey', location='headers')
parser.add_argument('chat_input', type=str, location='json')

@api.route('/api/demo')

class DemoResource(Resource):
    @api.expect(parser)
    def post(self):
        args = parser.parse_args()
        return {"chat_input": args['chat_input']}
        