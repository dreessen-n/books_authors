# __init__.py
from flask import Flask, render_template, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "Iron Maiden and Black Sabbath"
