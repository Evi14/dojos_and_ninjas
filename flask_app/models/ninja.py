from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def saveNinja(cls, data):
        query = "INSERT INTO ninjas (first_name , last_name, age, dojo_id, created_at, updated_at ) VALUES ( %(fname)s ,%(lname)s ,%(age)s ,%(dojo_id)s , NOW() , NOW());"
        return connectToMySQL('dojos_ninjas_schema').query_db( query, data )

    @classmethod
    def get_all(cls, data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s;"
        results = connectToMySQL('dojos_ninjas_schema').query_db(query, data)
        ninjas = []
        if not results:
            return ('')    
        for ninja in results:
            ninjas.append(cls(ninja))
        # print(ninjas)
        return ninjas
        