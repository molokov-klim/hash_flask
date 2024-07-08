from flask import Flask, request, jsonify
import subprocess
import logging

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
    return 'world', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
