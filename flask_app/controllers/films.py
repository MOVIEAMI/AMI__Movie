from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User 
from flask_app.models.film import Film 
from flask_app.models.category import Category
from flask_app.models.reservation import Reservation
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)




@app.route('/home')
def home():
    if 'user_id' not in session:                                  #check if i in session or not
        return redirect('/logout')
    
    data ={'id': session['user_id']}                              # put user id to session in data 
    one_user = User.get_one_by_id(data)                           # get information of user by id 
    all_show=Film.get_all()
    return  render_template("home_page.html", all_show=all_show , one_user=one_user)

# #-------------------------------------------------book_tikect.html
# @app.route ('/film/<int:id>')
# def show(id):
#     if 'user_id' not in session:                                  #check if i in session or not
#         return redirect('/logout')
#     print('--------------------------------------------------------------')
#     print(id)
#     data ={'id':id}                              # put user id to session in data 
#     one_film = Film.get_one_by_id(data)
#     print(one_film)
    
#     data_2 ={'id':id}  
#     one_user = User.get_one_by_id(data_2)

#     data_3={'id':id}  

#     one_category = Category.get_one_by_id(data_3)
#     print('--------------------------------------------------------------')

#     # get information of user by id 
# # all_show=film.get_all()
    
#     return  render_template("book_tikect.html",  one_user=one_user , one_film ,one_category=one_category )

#--------------------------------  go to page book tecket
@app.route('/book/<int:id>') #------------------------- route to register page
def book_ticket(id):
        # chek if id in session 
    if 'user_id' not in session:
        return redirect('/logout')
    # put id in date 
    data ={'id': session['user_id']}                              # put user id to session in data 
    one_user = User.get_one_by_id(data)
    data = {
        "id":id
    }
    
    one_film=Film.get_one_by_id(data)
    return  render_template("book_tikect.html", one_film=one_film , one_user=one_user)
#-------------------------------------------------------dashboard
@app.route('/dashbord')
def dash():
    if 'user_id' not in session:                                  #check if i in session or not
        return redirect('/logout')

    data ={'id': session['user_id']}                              # put user id to session in data 
    one_user = User.get_one_by_id(data)                           # get information of user by id 
    all_show=Film.get_join()
    return  render_template("dashboard.html", all_show=all_show , one_user=one_user)

    #----------------------------------add film

@app.route('/add/film') #------------------------- route to add_adimin_pag
def add_adimin_page():
        # chek if id in session 
    if 'user_id' not in session:
        return redirect('/logout')
    # put id in date 
    data ={'id': session['user_id']}                              # put user id to session in data 
    one_user = User.get_one_by_id(data)

    return  render_template("add_film.html", one_user=one_user)
#---------- ---------------------------------------------------------------route to cearte film
@app.route('/create/film',methods=['POST']) 
def create_films():
    if not Film.validation_film_admin(request.form): 
        return redirect('/add/film')
    print(request.form)
    data = {
        "name_film": request.form["name_film"],
        "description": request.form["description"],
        "director_name": request.form["director_name"],
        "broadcast_date": request.form["broadcast_date"],
        "broadcast_room": request.form["broadcast_room"],
        "category_id": request.form["category_id"],
        "url_image": request.form["url_image"],
        "price": int(request.form["price"]),
        "number_tickets": request.form["number_tickets"],
    }
    Film.create_film(data)
    return redirect('/dashbord')

# :::::::::::::::::::::::::::::::::::updaate pade
@app.route('/update/film/<int:id>')
def up_adimin_page(id):
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    film_one=Film.get_one_by_id(data)
    user_data = {
        "id":session['user_id']
    }

    return  render_template("update_film.html",film_one=film_one ,one_user=User.get_one_by_id(user_data))

# ----------------------------------------------------------------------------
@app.route('/up/film', methods=['POST']) # ::::::::::::::::::::::::::update film 
def update_film():
    if 'user_id' not in session:                                  #check if i in session or not
        return redirect('/logout')
    print('request.form')
    if not Film.validation_film_admin(request.form):
        show_id=request.form['id']
        return redirect(f'/update/film/{show_id}')

    data = {
        "name_film": request.form["name_film"],
        "description": request.form["description"],
        "director_name": request.form["director_name"],
        "broadcast_date": request.form["broadcast_date"],
        "broadcast_room": request.form["broadcast_room"],
        "category_id": request.form["category_id"],
        "url_image": request.form["url_image"],
        "price": request.form["price"],
        "number_tickets": request.form["number_tickets"],
    }
    Film.update_film(data)
    return redirect('/dashbord') 

    # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::delete film
@app.route('/destroy/film/<int:id>')
def destroy_flim(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Film.destroy_fiml(data)
    return redirect('/dashbord')


    #----------------------------------------------------- reservation 
@app.route('/filmsales')
def filmsales():
    if 'user_id' not in session:                                  #check if i in session or not
        return redirect('/logout')

    data ={'id': session['user_id']}                              # put user id to session in data 
    one_user = User.get_one_by_id(data)                           # get information of user by id 
    all_sales=Film.get_joinfilm()
    return  render_template("salesfilm.html", all_sales=all_sales , one_user=one_user)




