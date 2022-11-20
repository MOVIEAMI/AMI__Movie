from flask_app import app
from flask import render_template, redirect, request, session
from flask import flash
from flask_app.models.user import User
from flask_app.models.film import Film
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/') #------------------------- route to landing page
def landing_page():
    
    all_show=Film.get_all()
    print(all_show)
    return  render_template("landing_page.html" , all_show=all_show)

@app.route('/login') #------------------------- route to login page
def login_page():
    return  render_template("login.html")

@app.route('/register') #------------------------- route to register page
def register_page():
    return  render_template("register.html")

@app.route('/test') #------------------------- route to register page
def test():
    return  render_template("index.html")


@app.route('/add' , methods=['POST'] ) #------------route to check an add user information in data base
def add_user():
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    print(request.form)
    if not User.validate_register(request.form):                # function validation to verifail all input
        return redirect('/register')
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data ={                                                             # put info form in data 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash,
        "confirm_password": request.form['confirm_password'],
    }    
    print(pw_hash)
    id = User.save(data)                                        # insert in user data base
    session['user_id'] = id                                     # insert id user in session 

    return redirect('/login')


@app.route('/login/on', methods=['POST'])
def login():
    
    print(request.form)
    data = { "email" : request.form["email_login"] }
    user_in_db = User.get_one_by_email(data)
    
    if not user_in_db:
        flash("Invalid Email/password")
        return redirect("/login")
    print("************************************************")
    print (user_in_db.password)
    print(user_in_db.user_type)

    if not bcrypt.check_password_hash(user_in_db.password,request.form['password']):
        flash("Invalid Email/password")
        return redirect('/login')
    session['user_id'] = user_in_db.id
    if user_in_db.user_type == "user":
        return redirect('/home')

    return redirect("/dashbord")

#--------------------------------------------------------------------------------------------------route to go  dashbord
@app.route('/logout')
def logout():
        session.clear()
        return redirect('/')
