# controllers.books
from flask_app import app
from flask import Flask, render_template, request, redirect, session, url_for
from flask_app.models import author
from flask_app.models import book

# Create the routes
@app.route('/books')
def display_books():
    """Display the books page"""
    books = book.Book.display_all_books()
    print(books)
    return render_template('books.html', all_books=books)

@app.route('/books/create', methods=['POST'])
def add_book():
    """Add an book to the all_books"""
    if request.form['title'] == '' or request.form['num_of_pages'] == '':
        return redirect('/authors')
    data = {
        'title': request.form['title'],
        'num_of_pages': request.form['num_of_pages']
    }
    book.Book.create_book(data)
    return redirect('/books')

@app.route('/books/<int:id>')
def show_books_fav_authors(id):
    """
    Pass in book id
    Display the books with favorites authors and add to books's favorites 
    show authors who have not yet favorited the book
    """
    data = {
        'id': id
    }
    book_ = book.Book.get_book_and_author_fav(data)
    not_fav_author = author.Author.not_fav_author(data)
    return render_template('book_show.html', book=book_, not_fav_author=not_fav_author)

# TODO add to book author who is favorites it.
@app.route('/books/favorite', methods=['POST'])
def add_author_fav_to_book():
    """Add author who favorites the book"""
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    author.Author.add_fav_book(data)
    url = f"/books/{request.form['book_id']}"
    returnk("url")

# TODO set routes to UPDATE - UPDATE from db in models
# TODO set routes to DELETE - DELETE from db in models
