from flask import Flask, jsonify, request
from models import db, Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db.init_app(app)

# GET method to retrieve all books
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.serialize() for book in books])

# POST method to add a new book
@app.route('/books', methods=['POST'])
def add_book():
    title = request.json['title']
    author = request.json['author']
    new_book = Book(title=title, author=author)
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.serialize()), 201

# PATCH method to update an existing book
@app.route('/books/<int:book_id>', methods=['PATCH'])
def update_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    book.title = request.json.get('title', book.title)
    book.author = request.json.get('author', book.author)
    db.session.commit()
    return jsonify(book.serialize())

# DELETE method to delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted'})

if __name__ == '__main__':
    app.run(port= 5555)
