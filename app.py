from flask import Flask
from random import randint
import time
import flask_monitoringdashboard as dashboard

app = Flask(__name__)

dashboard.config.init_from(file='config.cfg')
# Make sure to call config.init_from() before bind()

def numberOfNewCustomers():
    return float(randint(1,5))

numberOfNewCustomers_schedule = {'seconds': 10}

#Run every day at midnight (use cron argument instead of interval)
#midnight_schedule = {'month':"*",
#                     'day': "*",
#                    'hour': 23,
#                   'minute': 59,
#                  'second': 00}


dashboard.add_graph("Every 10 Seconds", numberOfNewCustomers, "interval", **numberOfNewCustomers_schedule)
dashboard.bind(app)

@app.route('/')
def hello_world():
    return 'Flask-Monitoring-Dashboard tutorial'

@app.route('/endpoint1')
def endpoint1():
    time.sleep(0.20)
    return 'Endpoint1', 400

@app.route('/endpoint2')
def endpoint2():
    time.sleep(5)
    return 'Endpoint2'
