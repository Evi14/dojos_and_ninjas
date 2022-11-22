from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect("/dojos")

@app.route('/dojos')
def allDojos():
    dojos = Dojo.get_all()
    return render_template("read.html", all_dojos = dojos)

@app.route('/addDojo', methods=['post'])
def add_dojo():
    data = {
        "fname": request.form["fname"]
    }
    Dojo.save(data)
    return redirect('/dojos')
