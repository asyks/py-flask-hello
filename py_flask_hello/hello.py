#!/usr/bin/env python

from flask import Flask
from werkzeug.routing import Rule

from . import constants


app = Flask(__name__)

app.url_map.add(Rule("/", methods=("HEAD", "GET"), endpoint="index"))


@app.endpoint("index")
def index():
    return constants.SUCCESS_MESSAGE
