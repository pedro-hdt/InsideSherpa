"""
JPMC Virtual SEP - InsideSherpa - Module 1
Pedro Teixeira - O734271

REST API for the alerts package
Simplest usage example is to run this file as main, which starts a dev server. 
For proper deployment use a full WSGI server solution.
"""

from flask import Flask, request
from alerts import AlertService

app = Flask('alerts')

@app.route('/', methods=['POST'])
def validate(self):
    alert_service = AlertService()
    response = alert_service.alert_me(request.data)
    return response, 200

if __name__ == '__main__':
    app.run(debug=True)