# controllers.authors
# Import app
from flask_app import app
from flask import Flask, render_template, request, redirect, session, url_for
from flask_app.models import author
from flask_app.models import book

# Create the routes

@app.route('/')
def index():
    """Redirect homepage to authors page"""
    return redirect('/authors')

@app.route('/authors')
def display_authors():
    """Display the authors page as homepage"""
    authors = author.Author.display_all_authors()
    print(authors)
    return render_template('authors.html', all_authors=authors)

@app.route('/authors/create', methods=['POST'])
def add_author():
    """Add an author to the all_authors"""
    if request.form['name'] == '':
        return redirect('/authors')
    data = {
        'name': request.form['name']
    }
    author.Author.create_author(data)
    return redirect('/authors')

@app.route('/authors/<int:id>')
def show_author_fav(id):
    """
    Pass in author id
    Display the authors favorites and add to author's favorites 
    show books not yet favorited
    """
    data = {
        'id': id
    }
    author_ = author.Author.get_author_and_fav_books(data)
    not_fav_books = book.Book.not_fav_books(data)
    return render_template('author_show.html', author=author_, not_fav_books=not_fav_books)

# TODO add book to author fav
@app.route('/authors/favorite', methods=['POST'])
def add_book_to_author_fav():
    """Add book to the author's fav list"""
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    author.Author.add_fav_book(data)
    url = f"/authors/{request.form['author_id']}"
    return redirect('url')


# TODO set routes to UPDATE - UPDATE from db in models
# TODO set routes to DELETE - DELETE from db in models
