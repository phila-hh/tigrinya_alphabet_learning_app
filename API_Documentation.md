# Tigrinya Alphabet Learning API Documentation

---

## Overview

The Tigrinya Alphabet Learning API provides endpoints to access various resources related to the Tigrinya alphabet, including Tigrinya characters, character variations, audio pronunciations, and more. This documentation outlines the available endpoints, their functionalities, request parameters, and response formats.

---

## Base URL

The base URL for accessing the Tigrinya Alphabet Learning API is:

```
http://localhost:5000/api
```

---

## Endpoints

### 1. Get All Characters

- **URL:** `/characters`
- **Method:** `GET`
- **Description:** Retrieves all Tigrinya characters and their English representations.
- **Response Format:** JSON
- **Response Example:**
  ```json
  [
      {
          "character": "ሀ",
          "english_representation": "Ha"
      },
      {
          "character": "ለ",
          "english_representation": "Le"
      },
      ...
  ]
  ```

### 2. Get All Character Variations

- **URL:** `/character_variations`
- **Method:** `GET`
- **Description:** Retrieves all variations of all Tigrinya characters.
- **Response Format:** JSON
- **Response Example:**
  ```json
  {
      "ሀ": ["ሀ", "ሁ", "ሂ", "ሃ", "ሄ", "ህ", "ሆ"],
      "ለ": ["ለ", "ሉ", "ሊ", "ላ", "ሌ", "ል", "ሎ"],
      ...
  }
  ```

### 3. Get Character Variations by Character

- **URL:** `/character_variations/<character>`
- **Method:** `GET`
- **Description:** Retrieves all variations of a specific Tigrinya character.
- **Request Parameters:**
  - `character`: The Tigrinya character.
- **Response Format:** JSON
- **Response Example:**
  ```json
  {
      "ለ": ["ለ", "ሉ", "ሊ", "ላ", "ሌ", "ል", "ሎ"]
  }
  ```

### 4. Get Character Information

- **URL:** `/character/<character>`
- **Method:** `GET`
- **Description:** Retrieves the English representation of a specific Tigrinya character.
- **Request Parameters:**
  - `character`: The Tigrinya character.
- **Response Format:** JSON
- **Response Example:**
  ```json
  {
      "character": "ለ",
      "english_representation": "Le"
  }
  ```

### 5. Get Character Pronunciation

- **URL:** `/character/<character>/pronunciation`
- **Method:** `GET`
- **Description:** Retrieves the audio pronunciation of a specific Tigrinya character.
- **Request Parameters:**
  - `character`: The Tigrinya character.
- **Response Format:** Audio (WAV file)
- **Response Example:** Audio file download

---

## Usage

To use the Tigrinya Alphabet Learning API, send HTTP requests to the specified endpoints with appropriate parameters if required. The API will respond with the requested data or resources based on the provided parameters.

---

## Contact Information

For any inquiries or feedback regarding the Tigrinya Alphabet Learning API, please contact:

- **Author**: Filimon Haftom
- **Email**: filimon.haftomh@gmail.com
- **GitHub**: [phila-hh](https://github.com/phila-hh)
- **Twitter**: [@phila_hh](https://twitter.com/phila_hh)

Feel free to reach out for assistance, feedback, or collaboration!
