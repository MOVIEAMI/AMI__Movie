from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user 

class Category:
    db_name='ami_mouvies_schemas'
    def __init__(self,data):
        self.id = data['id']
        self.usre_id = data['usre_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_one_by_id(cls, data ):
        query = "SELECT * FROM Categories WHERE id = %(id)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        # print(result)
        return cls(result[0])

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users (first_name , last_name , email , password ) VALUES ( %(first_name)s , %(last_name)s , %(email)s ,%(password)s)"
        return connectToMySQL(cls.db_name).query_db( query, data )
        
