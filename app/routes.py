from flask import render_template
from app.Models import Book
import requests
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/book')
def book():
    endpoint = 'https://www.googleapis.com/books/v1/volumes?q=Climbing'
    response = requests.get(endpoint).json()
    bookList = []

    for book in response['items']:
        title = book['volumeInfo']['title']
        author = book['volumeInfo']['authors'][0]
        description = book['volumeInfo']['description']
        book = Book.Book(title, author, description)
        bookList.append(book)
    return render_template('index.html', title="Bookfinder", bookList=bookList)
