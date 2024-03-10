from flask import Flask, request
from flask_cors import cross_origin

from FileParser import FileParser

app = Flask(__name__)
    
@app.route('/api/compile', methods=['POST'])
@cross_origin()
def run_code():
    code = request.json['code']
    fileParser = FileParser("app.abg")
    outputs, errors = fileParser.run_from_script(code)
    
    return {'error': errors, 'output': outputs}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)