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


# TODO set routes to READ - SELECT from db in models
@app.route('/authors/<int:id')
def show_author_fav(id):
    """
    Pass in author id
    Display the authors favorites and add to author's favorites 
    show books not yet favorited
    """
    data = {
        'id': id
    }
    author = author.Author.get_author_and_fav_books(data)
    not_fav_books = book.Book.not_fav_books(data)
    return render_template('author_show.html', author= author, not_fav_books=not_fav_books)

# TODO set routes to UPDATE - UPDATE from db in models
# TODO set routes to DELETE - DELETE from db in models
