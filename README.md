# CodeAlpha_HangmanGame

## 📌 Project Title & Description
**Hangman Game — Countries Edition**

A console-based Hangman game built in Python, where the player guesses the name of a
country one letter at a time. Built using Object-Oriented Programming (OOP) as part of
the **CodeAlpha Python Programming Internship (Task 1)**.

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Clone this repository:
   ```bash
   git clone https://github.com/dhakshayine21-collab/CodeAlpha_HangmanGame.git
   cd CodeAlpha_HangmanGame
   ```
3. Run the game:
   ```bash
   python3 hangman.py
   ```
4. Follow the on-screen prompts and start guessing!

---

## 📜 Rules
- The game picks **1 random country** out of **5 predefined countries**.
- You guess **one letter at a time**.
- Correct letters are revealed in their position(s) in the word.
- You are allowed a maximum of **6 incorrect guesses**.
- Guess all the letters before running out of attempts to win.
- You may type `hint` once per round for a clue about the country.

---

## 🧠 Concepts Used
- **Object-Oriented Programming (OOP)** — game logic encapsulated in a `Hangman` class
- **`random` module** — randomly selecting the word each round
- **Sets** — tracking guessed letters efficiently
- **Dictionaries** — mapping each country to its hint
- **Loops & conditionals** — core game loop and win/lose logic
- **Input validation** — handling invalid, repeated, or empty input
- **String manipulation** — building the word display (`_ r a _ _ _`)

---

## 🖥️ Sample Terminal Output

```
==================================================
WELCOME TO HANGMAN: Countries Edition
Guess the country. You have 6 wrong guesses allowed.
Type 'hint' anytime for a clue (one hint per game).
==================================================

       ------
       |    |
       |
       |
       |
       |
    --------

Country: _ _ _ _ _ _
Wrong guesses remaining: 6

Guess a letter (or type 'hint'): f
Good guess! 'f' is in the word.

Country: f _ _ _ _ _
Wrong guesses remaining: 6
Letters guessed: f

Guess a letter (or type 'hint'): r
Good guess! 'r' is in the word.

Country: f r _ _ _ _
Wrong guesses remaining: 6
Letters guessed: f, r

Guess a letter (or type 'hint'): z
Sorry, 'z' is not in the word.

       ------
       |    |
       |    O
       |
       |
       |
    --------

Country: f r _ _ _ _
Wrong guesses remaining: 5
Letters guessed: f, r, z

...

Country: f r a n c e
🎉 Congratulations! You guessed the country: 'France'
```

---

## 🌍 Word List
`France` · `Japan` · `Brazil` · `Canada` · `Egypt`

---

## 👤 About
This project was built as part of the **CodeAlpha Python Programming Internship**,
demonstrating core Python fundamentals along with OOP design principles.

**Author:** [dhakshayine21-collab](https://github.com/dhakshayine21-collab)
