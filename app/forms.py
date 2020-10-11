from flask_wtf import Form
from wtforms import StringField, SelectField

class BookForm(Form):
    book_infos = [('Title', 'Title'),
               ('Author', 'Author'),
               ('Description', 'Description')]
    title = StringField('Title')
    author = StringField('Author')
    description = StringField('Description')
    book_info = SelectField('Info', choices = book_infos)

class BookSearchForm(Form):
    choices = [('Title', 'Title'),
           ('Author', 'Author'),
           ('Description', 'Description')]
    select = SelectField("Search for a book: ", choices = choices)
    search = StringField('')