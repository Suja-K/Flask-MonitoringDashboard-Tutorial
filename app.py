from flask import Flask
import time
import flask_monitoringdashboard as dashboard

app = Flask(__name__)
dashboard.config.init_from(file='config.cfg')
# Make sure to call config.init_from() before bind()
dashboard.bind(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/endpoint1')
def endpoint1():
    time.sleep(0.20)
    return 'Endpointw', 400

@app.route('/endpoint2')
def endpoint2():
    time.sleep(5)
    return 'Endpoint3'
