from flask import render_template
import pymongo
from app.main import bp  # noqa
from app.models.jdb import DB
import app.helperfunc
from pymongo import MongoClient
import json

client = MongoClient("mongodb://127.0.0.1:27017")
db = client["placeholder"]
h = app.helperfunc.Helper()
h = json.dumps()


@bp.route('/')
def index():
    """Main page route."""
    schematext = "Show Schema"
    return render_template('index.html', title = "AMI", 
        button_text = schematext, dbschema = h.getjsonschema('placeholder','Tests') )


@bp.route('/view_schema')
def add_job():
    """Shows Schema."""

    return ('', 204) 