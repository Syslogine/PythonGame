import os
import nltk
import random

nltk.download('words')

def choose_word(difficulty):
    words = nltk.corpus.words.words()
    
    if difficulty == 'easy':
        filtered_words = [word.lower() for word in words if 4 <= len(word) <= 6 and word.isalpha()]
    elif difficulty == 'medium':
        filtered_words = [word.lower() for word in words if 7 <= len(word) <= 9 and word.isalpha()]
    else:  # 'hard'
        filtered_words = [word.lower() for word in words if 10 <= len(word) and word.isalpha()]
    
    return random.choice(filtered_words)

def set_difficulty():
    while True:
        difficulty = input("Choose a difficulty level (easy/medium/hard): ").lower()
        if difficulty in ['easy', 'medium', 'hard']:
            return difficulty
        else:
            print("Invalid difficulty. Please choose easy, medium, or hard.")

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter.lower() in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def display_hangman(attempts):
    hangman_graphics = [
        '''
         ------
         |    |
         |
         |
         |
         |
         -
        ''',
        '''
         ------
         |    |
         |    O
         |
         |
         |
         -
        ''',
        '''
         ------
         |    |
         |    O
         |    |
         |
         |
         -
        ''',
        '''
         ------
         |    |
         |    O
         |   /|
         |
         |
         -
        ''',
        '''
         ------
         |    |
         |    O
         |   /|\\
         |
         |
         -
        ''',
        '''
         ------
         |    |
         |    O
         |   /|\\
         |   /
         |
         -
        ''',
        '''
         ------
         |    |
         |    O
         |   /|\\
         |   / \\
         |
         -
        '''
    ]
    max_index = len(hangman_graphics) - 1
    index_to_display = min(attempts, max_index)

    print(hangman_graphics[index_to_display])

def get_user_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        else:
            return guess

def play_again():
    response = input("Do you want to play again? (yes/no): ").lower()
    return response.startswith('y')

def main():
    while True:
        os.system('clear')  # Clear the screen for a cleaner interface
        difficulty = set_difficulty()

        if difficulty == 'easy':
            max_attempts = 8
        elif difficulty == 'medium':
            max_attempts = 6
        else:  # 'hard'
            max_attempts = 4

        guessed_letters = []
        word_to_guess = choose_word(difficulty)
        attempts = 0
        score = 0

        print(f"Welcome to Hangman! Difficulty: {difficulty.capitalize()}")
        print(display_word(word_to_guess, guessed_letters))

        while attempts < max_attempts:
            guess = get_user_guess(guessed_letters)
            guessed_letters.append(guess)

            if guess not in word_to_guess:
                attempts += 1
                print(f"Wrong guess! Attempts left: {max_attempts - attempts}")
                display_hangman(attempts)
            else:
                print("Good guess!")

            current_display = display_word(word_to_guess, guessed_letters)
            print(current_display)

            if current_display == word_to_guess:
                score += (max_attempts - attempts) * 10
                print(f"Congratulations! You guessed the word. Score: {score}")
                break

        if current_display != word_to_guess:
            print(f"Sorry, you ran out of attempts. The word was: {word_to_guess}")

        if not play_again():
            break

if __name__ == "__main__":
    main()
