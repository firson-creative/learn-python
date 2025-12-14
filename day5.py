from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    __tablename__ = 'books'
    id         = db.Column(db.Integer, primary_key=True)
    title      = db.Column(db.String(200), nullable=False, index=True)
    author     = db.Column(db.String(120), nullable=False)
    price      = db.Column(db.Numeric(10, 2), nullable=False, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

@app.route("/seed")
def seed():
    samples = [
        Book(title="Clean Code",              author="Robert C. Martin", price=39.99),
        Book(title="The Pragmatic Programmer",author="Andrew Hunt",      price=42.50),
        Book(title="Refactoring",             author="Martin Fowler",    price=47.25),
    ]
    db.session.add_all(samples)
    db.session.commit()
    return jsonify(message="saved", total=len(samples))

@app.route("/books")
def books():
    items = Book.query.order_by(Book.created_at.desc()).all()
    return jsonify([
        {"id": b.id, "title": b.title, "author": b.author, "price": float(b.price)}
       for b in items
        ])

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)