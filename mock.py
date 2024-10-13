import os
import time
import uuid
from cgitb import handler
from datetime import datetime


import flask
from flask import request
import json
import shutil
import logging

from logging.config import fileConfig
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


app = flask.Flask(__name__)

# hand = logging.handlers.RotatingFileHandler("logs/py_logs.log", maxBytes=2000, backupCount=10)
#
# logging.basicConfig(handlers=hand, level=logging.INFO, filename="logs/py_logs.log",  filemode="a", format = "%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s")
#

def create_rotating_log():
    fileConfig('logging_config.ini')
    logger = logging.getLogger()
    logger.debug('')



@app.route('/', methods=['GET'])
def main():
    return 'This url is for mock service, use POST method'


@app.route('/buy', methods=['POST', 'GET'])
def service():
    if request.method == 'POST':
        now = datetime.now()
        timestamp = int(round(now.timestamp()))
        random_uuid = str(uuid.uuid4())
        price = request.json["price"]
        method = request.method
        uri = request.url.split('/')[3]
        mydict = {"price": price, "message_id": random_uuid, "timestamp": timestamp, "method": method, "uri": "/"+uri}
        z = json.dumps(mydict)
        return z
    else:
        return 'This url is for mock service, use POST method'


if __name__ == '__main__':
    create_rotating_log()
    app.debug = True
    app.run(port=8099)
