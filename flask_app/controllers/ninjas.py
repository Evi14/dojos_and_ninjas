from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def ninjaPage():
    dojos = Dojo.get_all()
    return render_template("createNinja.html", all_dojos = dojos)

@app.route('/addNinja', methods=['post'])
def add_ninja():
    data = {
        "fname": request.form["fname"], 
        "lname": request.form["lname"], 
        "age": request.form["age"], 
        "dojo_id": request.form["dojo_id"]
    }
    Ninja.saveNinja(data)
    return redirect(f"/dojos/{data['dojo_id']}")

@app.route('/dojos/<int:id>')
def allNinjas(id):
    data ={ 
        "dojo_id":id
    }
    print(data["dojo_id"])
    ninjas = Ninja.get_all(data)
    print( Dojo.get_dojo(data))
    print(Ninja.get_all(data))
    dojo = Dojo.get_dojo(data)
    return render_template("dojoShow.html", all_ninjas = ninjas, dojo = dojo )
    