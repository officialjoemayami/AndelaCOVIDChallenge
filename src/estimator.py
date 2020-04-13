import sys
# import libaries
from flask import Flask, jsonify, request, make_response, got_request_exception
from flask_restful import Resource, Api
import json
import dicttoxml # customer lib from a github repo [https://github.com/quandyfactory/dicttoxml]

# import estimator
from api.v1.on_covid_19 import COVID
from res.log import LOG


# init app
app = Flask(__name__)
api = Api(app)

LOG.warning('dicttoxml')

# Start project here
class Estimator(Resource):  
  def post(self):
    # collect the data sent from endpoint
    data = request.json
    # initialize estimator with data collected from endpoint
    estimator = COVID(data)
    # call the estimator to work
    result = estimator.on_convid_19_estimator()
    # get the endpoint path used
    path = request.path
    # initialize your console log with path
    log = LOG(path)
    # log console with info log
    log.info()
  
    return jsonify({'output' : result.result()}) # the ouptut result

class JSONOutput(Resource):
  @api.representation('application/json')
  def post(self):
    # collect the data sent from endpoint
    data = request.json
    # initialize estimator with data collected from endpoint
    estimator = COVID(data)
    # call the estimator to work
    result = estimator.on_convid_19_estimator()
    # get the endpoint path used
    path = request.path
    # initialize your console log with path
    log = LOG(path)
    # log console with info log
    log.info()
    res = make_response(result.result())
    res.headers['Covid-19'] = 'Covid-19'
    res.status_code = 200
    res.mimetype = 'application/json'
    return res

class XMLOutput(Resource):
  @api.representation('application/xml')
  def post(self):
    # collect the data sent from endpoint
    data = request.json
    # initialize estimator with data collected from endpoint
    estimator = COVID(data)
    # call the estimator to work
    result = estimator.on_convid_19_estimator()
    # get the endpoint path used
    path = request.path
    # initialize your console log with path
    log = LOG(path)
    # log console with info log
    log.info()
    result = dicttoxml.dicttoxml(result.result())
    res = make_response(result)
    res.headers['Covid-19'] = 'Covid-19'
    res.status_code = 200
    res.mimetype = 'application/xml'
    return res
    
class COVIDLogs(Resource):
  @api.representation('application/text')
  def get(self):
    # get the endpoint path used
    path = request.path
    # initialize your console log with path
    log = LOG(path)
    # log console with info log
    log.info()
    with open('covid.log', 'r') as lf:
      result = lf.read()
    res = make_response(result)
    res.headers['Covid-19'] = 'Covid-19'
    res.status_code = 200
    res.mimetype = 'application/text'
    return res

# Endpoints and Rescources
api.add_resource(Estimator, '/api/v1/on-covid-19')
api.add_resource(JSONOutput, '/api/v1/on-covid-19/json')
api.add_resource(XMLOutput, '/api/v1/on-covid-19/xml')
api.add_resource(COVIDLogs, '/api/v1/on-covid-19/logs')

if __name__ == "__main__":
    app.run(debug=True)