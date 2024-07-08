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
    app.run(host='188.127.239.39', port=4001)
