from flask import flash, render_template, request, redirect
from app.Models import Book
from app.forms import BookSearchForm
import requests
from app import app


@app.route('/', methods = ['GET', 'POST'])
def index():
    search = BookSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template('index.html', form=search)


# @app.route('/results')
def search_results(search):
    search = BookSearchForm(request.form)
    results = []
    search_string = search.data['search']

    # display results
    endpoint = (f'https://www.googleapis.com/books/v1/volumes?q={search_string}')
    response = requests.get(endpoint).json()
    bookList = []

    for book in response['items']:
        title = book['volumeInfo']['title']
        author = book['volumeInfo']['authors'][0]
        description = book['volumeInfo']['description']
        book = Book.Book(title, author, description)
        bookList.append(book)
    return render_template('index.html', title="Bookfinder", bookList=bookList, form = search)



    # for book in response['items']:
   #     title = book['volumeInfo']['title']
    #    author = book['volumeInfo']['authors'][0]
     #   description = book['volumeInfo']['description']
      #  book = Book.Book(title, author, description)
       # bookList.append(book)
 #    return render_template('index.html', title="Bookfinder", bookList=bookList)