from flask import Flask
from flask import Response
from flask_cors import CORS
import os

app = Flask(__name__)

CORS(app)

@app.route('/')

def hello_world():
	return "Hello World"

@app.route('/233450')

def runPA():
	#os.system('"C:\Program Files (x86)\Steam\Steam.exe" steam://rungameid/233450')
	return "Running Prison Architect"

@app.route('/251570')

def run7dtd():
	#os.system('"C:\Program Files (x86)\Steam\Steam.exe" steam://rungameid/251570')
	return "Running 7 Days to Die"


if __name__ == "__main__":
	app.run()
	