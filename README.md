# Tigrinya Alphabet Learning App

---

## Overview

The Tigrinya Alphabet Learning App is a simple Flask-based application designed to assist users in learning the Tigrinya alphabet. This README.md file provides detailed information about the project, its purpose, structure, setup instructions, and functionalities.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Installation](#installation)
4. [Usage](#usage)
5. [API](#api)
5. [Contributing](#contributing)
6. [Contact Information](#contact-information)

---

## 1. Introduction

The Tigrinya Alphabet Learning App is a comprehensive platform designed to facilitate the learning process of the Tigrinya alphabet. Through interactive features and educational resources, users can learn the pronunciation of Tigrinya characters represented in English, accompanied by audio of actual pronunciation. This immersive experience enhances learning by providing both visual and auditory cues, allowing users to grasp the nuances of pronunciation effectively.

Additionally, the app offers a quiz section where users can test their knowledge and assess their understanding of the Tigrinya alphabet. By engaging in quizzes, users can reinforce their learning, identify areas for improvement, and track their progress over time. This interactive assessment tool adds an element of gamification to the learning process, making it engaging and rewarding for users of all proficiency levels.

The app also provides an API that allows developers to access audio pronunciations of Tigrinya characters programmatically, enabling integration with other applications or services.

---

## 2. Project Structure

The project structure is organized as follows:

- [`tal_app.py`](./tal_app.py): The main Flask application file containing the routes and logic.
- [`methods.py`](./methods.py): This module contains all the methods used to handle the Tigrinya characters.
- [`api/`](./api/): Directory containing API-related files.
- [`static/`](./static/): Directory containing static files (CSS, JS).
- [`templates/`](./templates/): Directory containing HTML templates.
- [`static/styles/`](./static/styles/): Directory containing CSS files.
- [`static/scripts/`](./static/scripts/): Directory containing JavaScript files.
- [`requirements.txt`](./requirements.txt): Contains all the dependancies required to run the web app.
- [`README.md`](./README.md): Comprehensive documentation for the project.
- [`API_Documentation.md`](./API_Documentation.md): Documentation for the API endpoints.

---

## 3. Installation

Follow the steps below to set up the Tigrinya Alphabet Learning App on your local machine:

1. Clone the repository:

   ```bash
   git clone https://github.com/phila-hh/tigrinya_alphabet_learning_app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd tigrinya_alphabet_learning_app
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## 4. Usage

To run the Tigrinya Alphabet Learning App, execute the following command:

```bash
python3 tal_app.py
```

Access the application in your web browser at `http://localhost:5000`.

---

## 5. API

The Tigrinya Alphabet Learning App provides an API that allows developers to access audio pronunciations of Tigrinya characters programmatically. The API endpoints are as follows:

- `/api/audio_pronunciations`: Retrieves all audio pronunciations of Tigrinya characters.

For more details on how to use the API, refer to the [API documentation](/API_Documentation.md).

---

## 6. Contributing

Contributions to the Tigrinya Alphabet Learning App project are welcome. Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Implement your changes.
4. Test thoroughly.
5. Create a pull request.

---

## 7. Contact Information

For any inquiries or feedback, please contact:

- **Author**: Filimon Haftom
- **Email**: filimon.haftomh@gmail.com
- **GitHub**: [phila-hh](https://github.com/phila-hh)
- **Twitter**: [@phila_hh](https://twitter.com/phila_hh)

Feel free to reach out for assistance, feedback, or collaboration!
