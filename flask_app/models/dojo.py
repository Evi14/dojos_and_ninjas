from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.ninjas = []
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name , created_at, updated_at ) VALUES ( %(fname)s , NOW() , NOW());"
        return connectToMySQL('dojos_ninjas_schema').query_db( query, data )

    @classmethod
    def get_dojo_with_ninjas( cls , data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_ninjas_schema').query_db( query , data )
        dojo = cls( results[0] )
        for row_from_db in results:
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "fname" : row_from_db["ninjas.fname"],
                "lname" : row_from_db["lname"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append( ninja.Ninja( ninja_data ) )
        return dojo
        
    @classmethod
    def get_dojo(cls, data):
        print(data)
        query = "SELECT name FROM dojos WHERE id = %(dojo_id)s;"
        results = connectToMySQL('dojos_ninjas_schema').query_db(query, data)
        return results[0]