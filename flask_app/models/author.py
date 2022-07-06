# models.author
from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models.ninja import Ninja

class Author:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # Create a list to store all the books associated with the instance of
        # A particular author
        self.books = []

    @classmethod
    def display_all_authors(cls):
        """Show all the authors"""
        query = "SELECT * FROM authors;"
        authors_from_db = connectToMySQL('books_authors_schema').query_db(query)
        authors = []
        for a in authors_from_db:
            authors.append(cls(a))
        return authors

    @classmethod
    def create_author(cls,data):
        """Create author based on data passed from form"""
        query = "INSERT INTO authors (name) VALUES (%(name)s);"
        return connectToMySQL('books_authors_schema').query_db(query,data)

    # @classmethod
    # def get_dojo_and_all_ninjas(cls,data):
    #     query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(dojo_id)s;"
    #     results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
    #     # Result will be a list of ninjas assigned to a particular dojo
    #     dojo = cls(results[0])
    #     for row_in_db in results:
    #         # Create instance of ninjas to add to list
    #         ninja_data = {
    #             'id': row_in_db['ninjas.id'],
    #             'first_name': row_in_db['first_name'],
    #             'last_name': row_in_db['last_name'],
    #             'age': row_in_db['age'],
    #             'created_at': row_in_db['ninjas.created_at'],
    #             'updated_at': row_in_db['ninjas.updated_at'],
    #             'dojo_id': row_in_db['dojo_id']
    #         }
    #         dojo.ninjas.append(Ninja(ninja_data))
    #     print(dojo)
    #     return dojo

