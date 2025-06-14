from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
BOOKS_FILE = 'books.json'


def load_books():
    if not os.path.exists(BOOKS_FILE):
        return []
    with open(BOOKS_FILE, 'r') as f:
        return json.load(f)


def save_books(books):
    with open(BOOKS_FILE, 'w') as f:
        json.dump(books, f, indent=4)


@app.route('/')
def index():
    books = load_books()
    return render_template('index.html', books=books)


@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        books = load_books()
        new_id = max([b['id'] for b in books], default=0) + 1
        new_book = {
            "id": new_id,
            "title": request.form['title'],
            "author": request.form['author'],
            "description": request.form['description'],
            "etat": request.form['etat'],
            "priorite": request.form['priorite'],
            "ref_number": request.form['ref_number'],
            "status": "disponible"
        }
        books.append(new_book)
        save_books(books)
        return redirect(url_for('index'))
    return render_template('add_book.html')


@app.route('/borrow/<int:book_id>', methods=['POST'])
def borrow_book(book_id):
    books = load_books()
    for book in books:
        if book['id'] == book_id and book['status'] == 'disponible':
            book['status'] = 'emprunté'
            break
    save_books(books)
    return redirect(url_for('index'))

@app.route('/delete/<book_id>', methods=['POST'])
def delete_book(book_id):
    books = load_books()
    books = [b for b in books if b['id'] != book_id]
    save_books(books)
    return redirect(url_for('index'))
    


if __name__ == '__main__':
    app.run(debug=True)
