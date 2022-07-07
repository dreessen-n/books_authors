# controllers.book
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