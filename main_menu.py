import importlib

def print_menu():
    print("Select a game to play:")
    print("1. Snake Game")
    print("2. Hangman Game")
    print("3. Tic-Tac-Toe Game")
    # Add more games as needed
    print("0. Quit")

def run_game(game_name):
    try:
        module = importlib.import_module(game_name)
        module.main()
    except ImportError:
        print(f"Error loading {game_name}.py. Make sure the file exists and contains a 'main' function.")

if __name__ == "__main__":
    while True:
        print_menu()
        choice = input("Enter the number of the game (or 0 to quit): ")

        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            run_game("snake_game.snake")
        elif choice == "2":
            run_game("hangman_game.hangman")
        elif choice == "3":
            run_game("tic_tac_toe_game.tic_tac_toe")
        # Add more game choices as needed
        else:
            print("Invalid choice. Please enter a valid option.")
