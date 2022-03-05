from asyncio import Event, events
from distutils.log import debug, set_verbosity
from sklearn import model_selection
from werkzeug.utils import secure_filename
import pandas as pd
from flask import Flask, render_template, request, redirect, jsonify, make_response

app = Flask(__name__)


@app.route("/", methods = ['POST', 'GET'])
def index():
    #home page for info and navigation
    return render_template("index.html")

@app.route("/sedan")
def sedan():
    #form information to model to render 
    #accept the user selection and display
    #make = float(request.form["Make"])
    #mileage = float(request.form["mileage"])

    #prediction = 0

    #X = [[make,mileage]]
    #filename= '../data/modelfilehere.sav'
    #loaded_model = pickle.load(open(filename, 'rb'))

    #prediction = loaded_model.predict(X)[0][0] ?? may not need bracketed 0
    #prediction = "${0:,.2f}".format(prediction)

    #Print(prediction) 
    return  render_template("sedan.html")  #in these para after html , prediction=prediction

@app.route("/truck")
def truck():
    #display drop down menu with states list
    #accept the user selection and display
    return render_template("truck.html")    

@app.route("/suv")
def suv():
    #display drop down menu with states list
    #accept the user selection and display 
    return render_template("suv.html")   

if __name__ == '__main__':
    app.run(debug=True)
