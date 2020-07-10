#!/usr/bin/python3

"""
JPMC Virtual SEP - InsideSherpa - Module 1
Pedro Teixeira - O734271

REST API for the alerts package
Simplest usage example is to run this file as main, which starts a dev server. 
For proper deployment use a full WSGI solution.
"""

import config

from flask import Flask, request
from alerts import AlertService

app = Flask('alerts_rest_api')

alert_service = config.get_alert_service()

@app.route('/', methods=['POST'])
def validate():
    response = []
    for line in request.data.decode().split('\n'):
        response.append(alert_service.alert_me(line))
    return '\n'.join(response), 200

app.run(debug=True)