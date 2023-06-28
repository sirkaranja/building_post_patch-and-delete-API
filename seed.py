from models import db, Book
from faker import Faker

fake = Faker()

def seed_data(num_books):
    db.create_all()

    for _ in range(num_books):
        title = fake.catch_phrase()
        author = fake.name()
        book = Book(title=title, author=author)
        db.session.add(book)

    db.session.commit()
