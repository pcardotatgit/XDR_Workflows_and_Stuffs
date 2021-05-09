from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
import os
from crayons import *

def jsonify_data(data):
    return jsonify({'data': data})


def jsonify_errors(data):
    return jsonify({'errors': [data]})
 
app = Flask(__name__)

@app.route('/')
def test0():
    return "<h1>RELAY MODULE IS UP</h1>"
    
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


@app.route('/health', methods=['POST'])
def health():   
    data = {'status': 'ok'}
    return jsonify({'data': data})    
    
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)