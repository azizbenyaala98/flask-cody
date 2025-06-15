from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
BOOKS_FILE = 'books.json'


def load_books():
    """
    Charger les livres depuis le fichier JSON.
    Retourner une liste vide si le fichier n'existe pas.
    """
    # À compléter par l'élève
    pass


def save_books(books):
    """
    Enregistrer les livres dans le fichier JSON.
    """
    # À compléter par l'élève
    pass


@app.route('/')
def index():
    """
    Page d'accueil : afficher la liste des livres.
    """
    # À compléter par l'élève
    pass


@app.route('/add', methods=['GET', 'POST'])
def add_book():
    """
    Affiche le formulaire d'ajout d'un livre (GET)
    ou enregistre un nouveau livre (POST).
    """
    # À compléter par l'élève
    pass


@app.route('/borrow/<int:book_id>', methods=['POST'])
def borrow_book(book_id):
    """
    Permet d'emprunter un livre s'il est disponible.
    """
    # À compléter par l'élève
    pass


@app.route('/delete/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    """
    Supprimer un livre de la collection.
    """
    # À compléter par l'élève
    pass


if __name__ == '__main__':
    app.run(debug=True)
