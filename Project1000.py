from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    published_date = db.Column(db.String(10), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'published_date': self.published_date
        }


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books]), 200


@app.route('/books', methods=['POST'])
def create_book():
    data = request.json
    new_book = Book(title=data['title'], author=data['author'], published_date=data.get('published_date'))
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201


@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify(book.to_dict()), 200


@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.json
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.published_date = data.get('published_date', book.published_date)
    db.session.commit()
    return jsonify(book.to_dict()), 200


@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'}), 204

if __name__ == '__main__':
    app.run(debug=True)