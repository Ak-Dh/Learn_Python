# 🧠 Quiz Game - Version 3

A simple terminal-based interactive quiz game in Python that supports multiple question types, tracks user scores, and now loads questions from an external JSON file.

---

## ✅ What's New in Version 3

Version 3 introduces **data separation** and **improved scalability** with the following changes:

### 📦 1. Questions Loaded from JSON

* Quiz questions are no longer hard-coded inside the Python script.
* All questions are now stored in a separate file: `questions.json`.
* This makes it easier to update, extend, or replace questions without touching the game logic.

### 💾 2. JSON Parsing Logic

* A new function `load_questions_from_file(filename)` has been added.
* It handles reading and parsing questions from a JSON file with error handling for:

  * Missing file
  * Invalid JSON format

### 🔁 3. Modular & Maintainable Code

* The game logic and data are now clearly separated.
* This sets a strong foundation for adding new features like:

  * Reading from a database
  * Loading questions based on difficulty or category

---

## 📁 File Structure

```
learn_python
├──quiz_game/
    ├──v3/
        ├── quiz_game.py          # Main Python script to run the game
        ├── questions.json        # External file containing all quiz questions
        └── README.md             # Project documentation
```

---

## 🧪 Supported Question Types

* ✅ QA (short answer)
* ✅ MCQ (multiple choice)

Support for more types (True/False, open-ended, etc.) is planned in future versions.