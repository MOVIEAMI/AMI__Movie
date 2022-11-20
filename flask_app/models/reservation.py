from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user 


class Reservation:
    db_name='ami_mouvies_schemas'
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.film_id = data['film_id']
        self.nb_reservation = data['nb_reservation'] 
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO reservations (user_id , film_id , nb_reservation) VALUES ( %(user_id)s , %(film_id)s , %(nb_reservation)s)"
        return connectToMySQL(cls.db_name).query_db( query, data )

    @classmethod
    def sum(cls, data ):
        query = "SELECT SUM(nb_reservation) FROM ami_mouvies_schemas.reservations where reservations.films_id=%(id)s ;"
        return connectToMySQL(cls.db_name).query_db( query, data )
    
