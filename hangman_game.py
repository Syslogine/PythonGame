import random

def choose_word():
    words = {
        'programming': 'Programming',
        'hangman': 'Hangman',
        'developer': 'Developer',
        'computer': 'Computer',
        'science': 'Science',
        'python': 'Python'
    }
    return random.choice(list(words.keys())), words

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
    print(hangman_graphics[attempts])

def hangman():
    max_attempts = 6
    guessed_letters = []
    word_to_guess, words = choose_word()
    attempts = 0
    score = 0

    print("Welcome to Hangman!")
    print(display_word(words[word_to_guess], guessed_letters))

    while attempts < max_attempts:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts += 1
            print(f"Wrong guess! Attempts left: {max_attempts - attempts}")
            display_hangman(attempts)
        else:
            print("Good guess!")

        current_display = display_word(words[word_to_guess], guessed_letters)
        print(current_display)

        if current_display == words[word_to_guess]:
            score += (max_attempts - attempts) * 10
            print(f"Congratulations! You guessed the word. Score: {score}")
            break

    if current_display != words[word_to_guess]:
        print(f"Sorry, you ran out of attempts. The word was: {words[word_to_guess]}")

if __name__ == "__main__":
    hangman()
