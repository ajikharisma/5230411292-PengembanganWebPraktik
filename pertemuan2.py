# IMPORT FLASK
from flask import Flask 

# Main app
app = Flask(__name__)

# set route untuk /
@app.route('/')

# function index
def index():
    return "Hello, World!"