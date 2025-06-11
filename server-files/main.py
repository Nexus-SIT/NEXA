from flask import Flask, jsonify, request
from tools import *
app = Flask(__name__)

@app.route('/check', methods=['GET'])
def check():
    return jsonify(message="Hey!,Im Nexa im Online")

@app.route('/web_search')
def greet():
    item=request.args.get('q')
    return jsonify(google_search(item))

if __name__ == '__main__':
    app.run(debug=True)