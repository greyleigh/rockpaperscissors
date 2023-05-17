import random

def get_player_choice():
    while True:
        choice = input("Enter your choice (Rock/Paper/Scissors), or 'I quit' to exit: ").strip().lower()
        if choice in ["rock", "paper", "scissors", "i quit"]:
            return choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Game Tied"
    elif (player_choice == "rock" and computer_choice == "paper") or \
         (player_choice == "scissors" and computer_choice == "rock") or \
         (player_choice == "paper" and computer_choice == "scissors"):
        return "You lose"
    else:
        return "You win"

def play_game():
    while True:
        player_choice = get_player_choice()
        if player_choice == "i quit":
            print("Thank you for playing.")
            break

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

# Start the game
play_game()
