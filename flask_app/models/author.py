# models.author
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # Create a list to store all the books associated with the instance of
        # A particular author
        self.fav_books = []

    @classmethod
    def display_all_authors(cls):
        """Show all the authors"""
        query = "SELECT * FROM authors;"
        authors_from_db = connectToMySQL('books_authors_schema').query_db(query)
        authors = []
        for a in authors_from_db:
            # Create an instance of author and append to list of authors
            authors.append(cls(a))
        return authors

    @classmethod
    def create_author(cls,data):
        """Create author based on data passed from form"""
        query = "INSERT INTO authors (name) VALUES (%(name)s);"
        return connectToMySQL('books_authors_schema').query_db(query,data)

    @classmethod
    def get_author_and_fav_books(cls,data):
        """Use LEFT JOINs to get author and all the books favorited by the author"""
        # get all from authors becuase need all values to manke an instance 
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON favorites.book_id = book.id WHERE authors.id = %(id)s;"
        results = connectToMySQL('books_authors_schema').query_db(query,data)
        # Result will be an author with associated favorite books
        # Create object instance of the author based on the first row returned
        author = cls(results[0])
        # Add all the favorite books to the instances fav_book list
        for row_in_db in results:
            # Add check for no favorites yet selected
            if row_in_db['books_id'] == None:
                # Possible add an alert to tell user no fav and redirect to authors page
                break
            # Create instance of book to add to list
            fav_book_data = {
                'id': row_in_db['books.id'],
                'title': row_in_db['title'],
                'num_of_pages': row_in_db['num_of_pages'],
                'created_at': row_in_db['books.created_at'],
                'updated_at': row_in_db['books.updated_at'],
            }
            author.fav_books.append(book.Book(fav_book_data))
        print(author)
        return author

