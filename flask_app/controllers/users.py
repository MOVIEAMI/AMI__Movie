from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User


@app.route('/') #------------------------- route to landing page
def landing_page():
    return  render_template("landing_page.html")

@app.route('/login') #------------------------- route to login page
def login_page():
    return  render_template("login.html")

@app.route('/login') #------------------------- route to register page
def register_page():
    return  render_template("register.html")


@app.route('/add' , methods=['POST'] ) #------------route to check an add user information in data base
def add_user():
    print(request.form)
    if not User.validate_register(request.form):                # function validation to verifail all input
        
        return redirect('/')
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data ={                                                    # put info form in data 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash,
        "confirm_password": request.form['confirm_password'],
    }    
    print(pw_hash)
    id = User.save(data)                                        # insert in user data base
    session['user_id'] = id                                     # insert id user in session 

    return redirect('/home')

#-------------------------------------------------------------------------route to go  dashbord
@app.route('/home')
def home():

    if 'user_id' not in session:                                  #check if i in session or not
        return redirect('/logout')
    
    data ={'id': session['user_id']}                              # put user id to session in data 
    one_user = User.get_one_by_id(data)                           # get information of user by id 
# all_show=film.get_all()
    return  render_template("dashbord.html", one_user=one_user)# , all_show=all_show)

