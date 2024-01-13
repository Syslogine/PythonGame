# Hangman Game in Python

This is a simple implementation of the classic Hangman game in Python. The game randomly selects a word from a predefined list, and the player has to guess the letters to complete the word within a limited number of attempts.

## Features

1. **Word Categories:** Each word belongs to a specific category (e.g., Programming, Developer, Science).
2. **Scoring System:** Players earn points based on the number of attempts left when they successfully guess the word.
3. **Visual Hangman Display:** A visual representation of the hangman is displayed as incorrect guesses accumulate.

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Syslogine/PythonGame.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd PythonGame
   ```

3. **Run the game:**

   ```bash
   python hangman_game.py
   ```

4. **Follow the on-screen instructions to guess the letters and complete the word.**

## Rules

- Players can only input single letters.
- The game provides feedback on correct and incorrect guesses.
- The player's score is based on the number of attempts remaining when the word is correctly guessed.

## Customization

Feel free to customize the game further:

- Modify the list of words in the `choose_word` function to include your own set of words.
- Add new word categories and corresponding words.
- Enhance the visual representation of the hangman.

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, feel free to fork the repository and submit a pull request.

## License

This Hangman game is licensed under the [MIT License](LICENSE).

Enjoy playing Hangman!
