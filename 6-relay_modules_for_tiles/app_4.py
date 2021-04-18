from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
from schemas import DashboardTileDataSchema, DashboardTileSchema
from utils import get_json, get_jwt, jsonify_data
import os
from crayons import *
import requests
import json

def paris_temperature():
    response=requests.get('https://www.prevision-meteo.ch/services/json/lat=46.259lng=5.235')
    payload=response.content
    json_payload=json.loads(payload)
    print(json_payload['current_condition']['date'])
    print(json_payload['current_condition']['hour'])
    print(json_payload['current_condition']['tmp'])
    return (json_payload['current_condition']['date'],json_payload['current_condition']['hour'],json_payload['current_condition']['tmp'])

def jsonify_data(data):
    return jsonify({'data': data})


def jsonify_errors(data):
    return jsonify({'errors': [data]})
 
app = Flask(__name__)

@app.route('/test')
def test():
    truc = 1 + 40
    return "<h1>Sounds Good the server is UP "+str(truc)+"</h1>"
    
    
@app.route('/test1')
def test1():
    truc = "toto"
    return "<h1>"+truc+"</h1>"

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404 

@app.route("/tiles", methods=["POST"])
def tiles():
    return jsonify_data(
        [
            {
                "id": "test-summary",
                "type": "metric_group",
                "title": "Tuile a Patrick - Paris Temperature",
                "periods": ["last_24_hours"],
                "short_description": "Paris Temperature",
                "description": "A longer description",
                "tags": ["test"],
            },
            {
                "id": "test-graph",
                "type": "line_chart",
                "title": "Test Graph",
                "periods": ["last_24_hours"],
                "short_description": "A short description",
                "description": "A longer description",
                "tags": ["test"],
            },
        ]
    )
    
@app.route("/tiles/tile-data", methods=["POST"])
def tile_data():
    data = get_json(DashboardTileDataSchema())
    print (green(data["tile_id"],bold=True))     
    if data["tile_id"] == "test-summary":
        date , hour , temp = paris_temperature()
        return jsonify_data(
            {
                "observed_time": {
                    "start_time": "2020-12-19T00:07:00.000Z",
                    "end_time": "2021-01-18T00:07:00.000Z",
                },
                "valid_time": {
                    "start_time": "2021-01-18T00:07:00.000Z",
                    "end_time": "2021-01-18T00:12:00.000Z",
                },
                "data": [
                    {
                        "icon": "brain",
                        "label": "Date",
                        "value": date,
                        "value-unit": "string",
                    },
                    {
                        "icon": "percent",
                        "label": "hour",
                        "value": hour,
                        "value-unit": "string",
                    },
                    {
                        "icon": "percent",
                        "label": "Temperature",
                        "value": temp,
                        "value-unit": "integer",
                    },                    
                ],
                "cache_scope": "org",
            }
        )
    else:
        return jsonify_data(
            {
                "observed_time": {
                    "start_time": "2020-12-28T04:33:00.000Z",
                    "end_time": "2021-01-27T04:33:00.000Z",
                },
                "valid_time": {
                    "start_time": "2021-01-27T04:33:00.000Z",
                    "end_time": "2021-01-27T04:38:00.000Z",
                },
                "key_type": "timestamp",
                "data": [
                    {"key": 1611731572, "value": 13},
                    {"key": 1611645172, "value": 20},
                    {"key": 1611558772, "value": 5},
                    {"key": 1611431572, "value": 13},
                    {"key": 1611345172, "value": 20},
                    {"key": 1611258772, "value": 5},
                    {"key": 1611131572, "value": 13},
                    {"key": 1611045172, "value": 20},
                    {"key": 1610958772, "value": 5},
                    {"key": 1610831572, "value": 13},
                    {"key": 1610745172, "value": 20},
                    {"key": 1610658772, "value": 5},
                    {"key": 1610531572, "value": 13},
                    {"key": 1610445172, "value": 20},
                    {"key": 1610358772, "value": 5},
                ],
                "cache_scope": "org",
            }
        )
         

@app.route('/health', methods=['POST'])
def health():   
    data = {'status': 'ok'}
    return jsonify({'data': data})    
    
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)