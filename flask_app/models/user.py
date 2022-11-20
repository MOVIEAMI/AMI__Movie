from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re	  
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    db_name='ami_mouvies_schemas'
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.password = data['password']
        self.email = data['email']
        self.user_type = data['user_type']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
#----------------------------------------------
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users (first_name , last_name , email , password ) VALUES ( %(first_name)s , %(last_name)s , %(email)s ,%(password)s)"
        return connectToMySQL(cls.db_name).query_db( query, data )


    
#----------------------  get  user by id

    @classmethod
    def get_one_by_id(cls, data ):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(result[0])

#--------------------------------------------- get user by mail
    @classmethod
    def get_one_by_email(cls, data ):
            query =" SELECT *FROM users WHERE email =%(email)s;"
            result =connectToMySQL(cls.db_name).query_db( query, data )
            if len(result)<1:
                return False
            return cls(result[0])


#-----------------------------------Update user

    @classmethod
    def update_user(cls,data):
        print(data, '*'*20)
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s ,email=%(email)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

#--------------------------------------------validate input
    @staticmethod
    def validate_register(data):
        is_valid = True
        query="SELECT * FROM users WHERE email = %(email)s ;"
        result = connectToMySQL(User.db_name).query_db(query,data)
        if len(result)>=1:
            flash("Email Already Exist")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']): 
            flash("Incorrect Email")
            print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            is_valid = False
        if len(data['first_name']) < 2:
            print("wronnnnnnnnnnnnnnnnnnnng")
            flash("first Name must be at least 2 characters." )
            is_valid = False
        if len(data['last_name']) < 2:
            flash("last name must be at least 2 characters.")
            is_valid = False
        if len(data['password']) < 3:
            flash("password must be at least 8 characters.")
            is_valid = False
        if data['password'] != data['confirm_password']:
            flash("Passwords don't match")
            is_valid = False
        return is_valid


        #------------------------------------
    @staticmethod
    def validate(data):
        is_valid = True # we assume this is true.
        query="SELECT * FROM users WHERE email = %(email)s ;"
        result = connectToMySQL(User.db_name).query_db(query,data)
        if len(result)>=1:
            flash("Email Already Exist")
        if not EMAIL_REGEX.match(data['email']): 
            flash("Incorrect Email", 'email')
            is_valid = False
        if len(data['first_name']) < 2:
            flash("first Name must be at least 2 characters." )
            is_valid = False
        if len(data['last_name']) < 2:
            flash("last name must be at least 2 characters.")
            is_valid = False
        return is_valid


        #-----------------------------------
        # -------------------------------------------------------------------------logout admin 
    