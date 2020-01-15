from flask import Flask
from flask import Response
from flask_cors import CORS
import os

app = Flask(__name__)

CORS(app)

@app.route('/')

def hello_world():
	return "Hello World"

@app.route('/game')

def steamStream():
	os.system('"C:\Program Files (x86)\Steam\Steam.exe" steam://rungameid/233450')
	return "Steam Game"


if __name__ == "__main__":
	app.run()