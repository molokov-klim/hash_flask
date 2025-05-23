"""
This is main flask module - entry point of app
"""
# pylint: disable=import-error
from flask import Flask


app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
    """
    hello world end-point
    """
    return 'world', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4022)
