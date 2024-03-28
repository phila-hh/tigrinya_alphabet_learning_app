"""
Module Documentation: tal_app.py

Tigrinya Alphabet Learning Web App

This web application allows users to learn the Tigrinya alphabet through interactive exercises and quizzes.

It consists of the following components:
1. Landing Page: Provides an introduction to the web app.
2. Index Page: Serves as the main page with navigation links.
3. Learn Tigrinya Page: Allows users to select Tigrinya characters to learn.
4. Learn Page: Provides selected characters and their variation, with their english representation and actual audio pronunciation.
5. Practice Quiz Page: Allows users to select Tigrinya characters for the quiz.
6. Quiz Page: Provides a practice quiz for users to test their knowledge..

Author: Filimon Haftom
Date: March 27, 2024

"""
from flask import Flask, render_template, request, session, redirect
import secrets
import methods

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = secrets.token_hex(32)

@app.route('/')
def landing_page():
    """
    Renders the landing page of the Tigrinya Alphabet Learning web app.

    Returns:
        HTML template: landing_page.html
    """
    return render_template('landing_page.html', value=None)


@app.route('/index')
def index():
    """
    Renders the index page of the Tigrinya Alphabet Learning web app.

    Returns:
        HTML template: index.html
    """
    return render_template('index.html')


@app.route('/learn_tigrinya', methods=['GET', 'POST'])
def learn_tigrinya():
    """
    Renders the page for selecting Tigrinya characters to learn.

    If the form is submitted, it processes the selected characters and redirects to the learning page.

    Returns:
        HTML template: learn_tigrinya.html
    """
    session.pop('selected_characters', None)  # Clear previously selected characters
    characters = methods.TIGRINYA_CHARACTERS
    english_representations = methods.ENG_REPRESENTATION
    return render_template('learn_tigrinya.html', zipped=methods.zip_characters(characters, english_representations))


@app.route('/practice_quiz', methods=['GET', 'POST'])
def practice_quiz():
    """
    Renders the practice quiz page of the Tigrinya Alphabet Learning web app.

    Returns:
        HTML template: practice_quiz.html
    """
    session.pop('selected_characters', None)
    return render_template('practice_quiz.html', tigrinya_characters=methods.TIGRINYA_CHARACTERS)


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    """
    Renders the quiz page of the Tigrinya Alphabet Learning web app.

    If the form is submitted, it processes the selected characters and displays quiz results.

    Returns:
        HTML template: quiz.html
    """
    if request.method == 'POST':
        selected = [char for char, selected in zip(methods.TIGRINYA_CHARACTERS, request.form.getlist('selected_characters')) if selected == '1']
        if len(selected) == 0:
            selected = methods.random_chars()
        selected_characters = methods.selected_characters(selected)
        english_representations = methods.selected_eng_representations(selected)
        return render_template('quiz.html', zipped=methods.zip_characters(selected_characters, english_representations))
    else:
        return render_template('practice_quiz.html', tigrinya_characters=methods.TIGRINYA_CHARACTERS)


@app.route('/learn', methods=['GET', 'POST'])
def learn():
    """
    Renders the learning page of the Tigrinya Alphabet Learning web app.

    If the form is submitted, it processes the selected characters and displays learning results.

    Returns:
        HTML template: learn.html or learn_tigrinya.html
    """
    if request.method == 'POST':
        selected = [char for char, selected in zip(methods.TIGRINYA_CHARACTERS, request.form.getlist('selected_characters')) if selected == '1']
        if len(selected) == 0:
            selected = methods.random_chars()
        selected_characters = methods.selected_characters(selected)
        english_representations = methods.selected_eng_representations(selected)
        return render_template('learn.html', zipped=methods.zip_characters(selected_characters, english_representations))
    else:
        return render_template('learn_tigrinya.html', tigrinya_characters=methods.TIGRINYA_CHARACTERS)


if __name__ == "__main__":
    """ Main function """
    app.run(debug=True)
