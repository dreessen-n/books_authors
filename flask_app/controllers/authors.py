# Import app
from flask_app import app
from flask import Flask, render_template, request, redirect, session, url_for
from flask_app.models import author

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

# TODO set routes to CREATE - INSERT into db in models
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
# TODO set routes to UPDATE - UPDATE from db in models
# TODO set routes to DELETE - DELETE from db in models
