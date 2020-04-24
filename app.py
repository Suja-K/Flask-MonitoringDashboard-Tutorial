from flask import Flask
import flask_monitoringdashboard as dashboard

app = Flask(__name__)
dashboard.config.init_from(file='config.cfg')
# Make sure to call config.init_from() before bind()
dashboard.bind(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'
