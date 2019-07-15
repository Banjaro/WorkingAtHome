from flask import render_template
import pymongo
from app.main import bp  # noqa
from app.helperclass import Helper
from pymongo import MongoClient
import json

h = Helper()

@bp.route('/')
def index():
    """Main page route."""
    return render_template('index.html', title = "AMI", 
        dbschema = h.getjsonschema('placeholder','Tests'))