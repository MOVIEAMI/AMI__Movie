from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User 
from flask_app.models.film import Film 
from flask_app.models.category import Category
from flask_app.models.reservation import Reservation
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route ('/film/reservation' , methods=['POST'])
def reservation():

    print(request.form)
    data ={                                                             # put info form in data 
        "user_id": request.form['user_id'],
        "film_id": request.form['film_id'],
        "nb_reservation": request.form['nb_reservation'],
    }    
    id = Reservation.save(data)

    return  redirect("/home")