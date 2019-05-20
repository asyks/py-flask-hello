#!/usr/bin/env python

from flask import Flask

from . import constants


app = Flask(__name__)


@app.route("/")
def hello():
    return constants.SUCCESS_MESSAGE
