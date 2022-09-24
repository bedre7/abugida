from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from FileParser import FileParser

app = Flask(__name__)
CORS(app)

@app.route('/api/input', methods=['POST'])
@cross_origin()
def run_code():
    code = request.json['code']
    fileParser = FileParser("app.abg")

    outputs, errors = fileParser.run_from_script(code)
    
    return {'error': errors, 'output': outputs}

if __name__ == '__main__':
    app.run()