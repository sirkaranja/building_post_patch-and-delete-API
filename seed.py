from app import app
from models import db, Book
from faker import Faker

fake = Faker()

def seed_data(num_books):
    with app.app_context():
        db.create_all()

        for _ in range(num_books):
            title = fake.catch_phrase()
            author = fake.name()
            book = Book(title=title, author=author)
            db.session.add(book)

        db.session.commit()

if __name__ == '__main__':
    seed_data(10)
