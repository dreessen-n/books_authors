# models.book
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author, book

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # Store authors who favorited the book
        self.authors_favs = []

    @classmethod
    def display_all_books(cls):
        """"Show all the books"""
        query = "SELECT * FROM books;"
        books_from_db = connectToMySQL('books_authors_schema').query_db(query)
        books = []
        for b in books_from_db:
            # Create an instance of book and append to list of books
            books.append(cls(b))
        return books

    @classmethod
    def create_book(cls,data):
        """Create book based on data passed from form"""
        query = "INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s);"
        return connectToMySQL('books_authors_schema').query_db(query,data)

    @classmethod
    def get_book_and_author_fav(cls, data):
        """Use LEFT JOINs to get book and all the authors who favorited it."""
        # get all from books becuase need all values to manke an instance 
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s;" 
        results = connectToMySQL('books_authors_schema').query_db(query,data)
        # Result will be a book with associated favorites from authors
        # Create an instance of book based on the first row of the data returned
        book = cls(results[0])
        # Add all the authors who favorited the book to the authors_fav list
        for row_in_db in results:
            # Add check for no favorite from authors
            # if row_in_db['author_id'] == None:
                # Possible to add alert to tell user no fav and to redirect back to book page
                # break
            # Create instance of author to add to list
            author_fav_data = {
                'id': row_in_db['author_id'],
                'name': row_in_db['name'],
                'created_at': row_in_db['created_at'],
                'updated_at': row_in_db['updated_at']
            }
            book.authors_favs.append(author.Author(author_fav_data))
            print(book)
            return book

    @classmethod
    def not_fav_books(cls,data):
        """Get the list of books not favorited by author"""
        query = "SELECT * FROM books WHERE books.id NOT IN (SELECT book_id FROM favorites WHERE author_id=%(id)s);"
        # Save results of the query
        results = connectToMySQL('books_authors_schema').query_db(query,data)
        # Create list for not_fav_books
        not_fav_books = []
        # Iterate thru the results to add each not fav book instance to the list
        for row_in_db in results:
            not_fav_books.append(cls(row_in_db))
        return not_fav_books


