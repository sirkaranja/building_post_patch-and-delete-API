from flask import Flask, jsonify, request
from models import db, Book
from seed import seed_data

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


#Get method to retrive all books
@app.route('/books', methods=['GET'])
def get_books():
    books= Book.query.all()
    return jsonify([book.serialize()for book in books])



if __name__ =='__main__':
    app.run(port=5555)