from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user 
import re	  
EMAIL_REGEX = re.compile(r'^[0-9]')


class Film:
    db_name='ami_mouvies_schemas'
    def __init__(self,data):
        self.id = data['id']
        self.name_film = data['name_film']
        self.description = data['description']
        self.director_name = data['director_name']
        self.broadcast_date = data['broadcast_date']
        self.broadcast_room = data['broadcast_room']
        self.url_image = data['url_image'] 
        self.price = data['price']
        self.number_tickets= data['number_tickets']
        self.category_id =data['category_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        

#----------------------  get  one film  by id

    @classmethod
    def get_one_by_id(cls, data ):
        query = "SELECT * FROM films WHERE id = %(id)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(result[0])

#-------------------------- get all films
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM films;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_films = []
        for row in results:
            all_films.append( cls(row) )
            print(row)
        return all_films


    #---------------------------------------------- create film
    @classmethod
    def create_film(cls, data ):
        query = "INSERT INTO films (name_film , description , director_name , broadcast_date, broadcast_room , category_id , url_image, price , number_tickets ) VALUES ( %(name_film)s , %(description)s , %(director_name)s ,%(broadcast_date)s , %(broadcast_room)s, %(category_id)s, %(url_image)s, %(price)s, %(number_tickets)s ) ;"
        return connectToMySQL(cls.db_name).query_db( query, data )

    #---------------------------- select by join
    @classmethod
    def get_join(cls):
        query = "SELECT * FROM films JOIN categories ON categories.id = films.category_id;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        print(results)
        return results

    #----------------------------------------------------------------------delete film
    @classmethod
    def destroy_fiml(cls,data):
        query  = "DELETE FROM ami_mouvies_schemas.films WHERE  id= %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
#-----------------------------------Update films 
    @classmethod
    def update_film(cls,data):
        query = "UPDATE films SET name_film =%(name_film)s, description =%(description)s , director_name=%(director_name)s , broadcast_date=%(broadcast_date)s, broadcast_room=%(broadcast_room)s , category_id =%(category_id)s , url_image =%(url_image)s, price =%(price)s,  number_tickets=%(number_tickets)s  WHERE name_film = %(name_film)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)


    #--------------------------------------------validame_filmate films
    @staticmethod
    def validation_film_admin(data):
            is_valname_film = True

            
            if len(data['name_film']) < 2:
                flash(" the Name of Film must be at least 2 characters.",'films' )
                is_valname_film = False
            if len(data['description']) < 10:
                flash("Description must be at least 10 characters.",'films' )
                is_valname_film = False
            if len(data['description']) > 255:
                flash(" your Description ti is to longe.",'films' )
                is_valname_film = False
            if len(data['director_name']) < 3:
                flash("the Director Name must be at least 3 characters.",'films' )
                is_valname_film = False
            if data['broadcast_date'] == "":
                flash("Please enter a date.",'films' )
                is_valname_film = False
            if len(data['broadcast_room']) < 2:
                flash(" select the place of the show .",'films' )
                is_valname_film = False
            if len(data['category_id']) <1:
                flash("selelect the category of the film.",'films' )
                is_valname_film = False
            if len(data['url_image']) < 3:
                flash(" put url_image .",'films' )
                is_valname_film = False
            if not EMAIL_REGEX.match(data['price']): 
                flash("the price shoold be a number", 'films')
                is_valname_film = False
            if len(data['price']) < 1:
                flash("price must be at least 1 .",'films' )
                is_valname_film = False
            if not EMAIL_REGEX.match(data['number_tickets']): 
                flash("the price shoold be a number", 'films')
                is_valname_film = False
            if len(data['number_tickets']) < 1:
                flash("price must be at least 1 .",'films' )
                is_valname_film = False
            return is_valname_film



            #----------------------------------------------select user films nb_reservation
    @classmethod
    def get_joinfilm(cls):
        query = "SELECT * FROM reservations JOIN users ON users.id = reservations.user_id join films on reservations.film_id = films.id;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        print(results)
        return results