"""
Hangman Game (Upgraded - Countries Edition)
CodeAlpha Python Programming Internship - Task 1

An object-oriented, console-based Hangman game where the player
guesses the name of a country one letter at a time.
Rules: 5 predefined words, 6 incorrect guesses allowed.
"""

import random


class Hangman:
    """Encapsulates all state and behavior for a single Hangman game."""

    MAX_WRONG_GUESSES = 6

    # Step 1: Predefined word list -> 5 countries, each with a short hint
    WORD_BANK = {
        "france": "Famous for the Eiffel Tower",
        "japan": "Known as the Land of the Rising Sun",
        "brazil": "Home to the Amazon Rainforest",
        "canada": "Known for maple syrup and maple leaves",
        "egypt": "Home of the ancient pyramids",
    }

    HANGMAN_STAGES = [
        """
       ------
       |    |
       |
       |
       |
       |
    --------
        """,
        """
       ------
       |    |
       |    O
       |
       |
       |
    --------
        """,
        """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
        """,
        """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
        """,
        """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
        """,
        """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
        """,
        """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
        """,
    ]

    def __init__(self):
        self.word, self.hint = self._choose_word()
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.hint_used = False

    def _choose_word(self):
        """Step 2 & 3: Randomly select a country and its hint from the word bank."""
        word = random.choice(list(self.WORD_BANK.keys()))
        return word, self.WORD_BANK[word]

    @property
    def remaining_guesses(self):
        return self.MAX_WRONG_GUESSES - self.wrong_guesses

    @property
    def is_won(self):
        return all(letter in self.guessed_letters for letter in self.word)

    @property
    def is_lost(self):
        return self.wrong_guesses >= self.MAX_WRONG_GUESSES

    def display_word(self):
        """Step 4: Build the current display, e.g. '_ r _ n c e'."""
        return " ".join(
            letter if letter in self.guessed_letters else "_" for letter in self.word
        )

    def show_status(self):
        """Print the hangman drawing, word progress, and guess info."""
        print(self.HANGMAN_STAGES[self.wrong_guesses])
        print("Country: " + self.display_word())
        print(f"Wrong guesses remaining: {self.remaining_guesses}")
        if self.guessed_letters:
            print(f"Letters guessed: {', '.join(sorted(self.guessed_letters))}")
        print()

    def get_player_guess(self):
        """
        Step 5: Ask the player for a single letter (or 'hint').
        Validates: must be one alphabet letter, not guessed already.
        """
        while True:
            guess = input("Guess a letter (or type 'hint'): ").lower().strip()

            if guess == "hint":
                if self.hint_used:
                    print("You've already used your hint for this round.\n")
                else:
                    print(f"Hint: {self.hint}\n")
                    self.hint_used = True
                continue

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single letter.\n")
                continue

            if guess in self.guessed_letters:
                print(f"You already guessed '{guess}'. Try a different letter.\n")
                continue

            return guess

    def apply_guess(self, guess):
        """Step 6: Update game state based on the guessed letter."""
        self.guessed_letters.add(guess)
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.\n")
        else:
            self.wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.\n")

    def reveal_word(self):
        print(" ".join(self.word))


def play_round():
    """Runs a single game of Hangman from start to finish."""
    game = Hangman()

    print("=" * 50)
    print("WELCOME TO HANGMAN: Countries Edition")
    print(f"Guess the country. You have {Hangman.MAX_WRONG_GUESSES} wrong guesses allowed.")
    print("Type 'hint' anytime for a clue (one hint per game).")
    print("=" * 50)

    while True:
        game.show_status()
        guess = game.get_player_guess()
        game.apply_guess(guess)

        if game.is_won:
            game.show_status()
            print(f"🎉 Congratulations! You guessed the country: '{game.word.title()}'")
            break

        if game.is_lost:
            game.show_status()
            print("💀 Game over! You've run out of guesses.")
            print(f"The country was: '{game.word.title()}'")
            break


def main():
    """Entry point: runs rounds until the player chooses to stop."""
    while True:
        play_round()
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != "y":
            print("Thanks for playing! Goodbye.")
            break
        print("\n")


if __name__ == "__main__":
    main()
