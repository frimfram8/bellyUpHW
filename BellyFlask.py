# import necessary libraries
import pandas as pd
import numpy as np
from flask import (
    Flask,
    render_template,
    jsonify,
    request)

from flask_sqlalchemy import SQLAlchemy
#I have zero idea how sqlalchemy is being used here...

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Database Setup
#################################################
app.config['belly_button_biodiversity'] = "sqlite:///db.sqlite"

db = SQLAlchemy(app)


class Belly(db.Model):
    __tablename__ = 'bellyUp'

    otu = db.Column(db.Integer())
    samples = db.Column(db.String(150))
    samples_metadata = db.Column(db.String(150))



@app.before_first_request
def setup():
    db.create_all()


#################################################
# Routes
#################################################

@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")


#list of sample names in format BB_450 etc.
@app.route("/names")
def names():
    results = db.session.query(bellyUp.samples).all()

    name_list = []
    for result in results:
        name_list.append({
            "name": result[0]
        })
    return jsonify(names)
    #when do I jsonify things and when do I not? No idea. Also no idea really what to call from results lines in these...


#otu descriptions
@app.route("/otu")
def otu():
    results = db.session.query(bellyUp.otu_id).all()

    otus = []
    for result in results:
        otus.append({
            "otu": result[0]
        })
    return jsonify(otu)


#metadata for specific sample in json format
@app.route("/metadata/<sample>")
def metadata():
    results = db.session.query(bellyUp.AGE, bellyUp.BBTYPE, bellyUp.ETHNICITY, bellyUp.GENDER, bellyUp.LOCATION, bellyUp.SAMPLEID).all()

    metadata_samples = []
    for result in results:
        metadata_samples.append({
            "age": result[0],
            "bb_type": result[1],
            "ethnicity": result[2],
            "gender": result[3],
            "location": result[4],
            "sample_id": result[5]        })
    return jsonify(metadata)


#weekly washing frequency as a number
@app.route("/wfreq/<sample>")
def wfreq():
    results = db.session.query(bellyUp.WFREQ).all()

    wash_freq = []
    for result in results:
        wash_freq.append({
            "wash_freq": result[0]
        })
    return jsonify(wfreq)


#otu ids and sample values
@app.route("/samples/<sample>")
def samples():
    results = db.session.query(bellyUp.otu_id, bellyUp.sample_value).all()

    sample_list = []
    for result in results:
        sample_list.append({
            "otu_id": result[0],
            "sample_value": result[1]
        })
    return jsonify(samples)


if __name__ == "__main__":
    app.run()
