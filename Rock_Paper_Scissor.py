import random

# Define the choices and their corresponding symbols
choices = {
    '1': 'Rock 🪨',
    '2': 'Paper 📄',
    '3': 'Scissors ✂️'
}

# Function to determine the result of the game
def get_result(user_choice, computer_choice):
    if user_choice not in choices:
        return "\nInvalid choice. ❌ Please try again."

    if choices[user_choice] == computer_choice:
        return "\nIt's a tie! 🤝"

    # Define win conditions for user
    win_conditions = {
        'Rock 🪨': 'Scissors ✂️',
        'Paper 📄': 'Rock 🪨',
        'Scissors ✂️': 'Paper 📄'
    }

    if win_conditions[choices[user_choice]] == computer_choice:
        return f'\nBroave {user_name}, You win... 😎 {virtual_player} lose...😞'
      
    else:
        return f"\nOops! {user_name}, You lose...😞 {virtual_player} win...😎"

# User Interface
print("Welcome to the game! 🎮")
print("-----------------------")

print("\nIf you're new to the game, please read the rules below:\nThere will be 2 characters: 'You' and a 'Virtual Player(Computer)'.\n(rock beats scissors, scissors beats paper, and paper beats rock)")

print("\n******************************************")
print("\nIf you're ready, let's start the game! 🎮")

# Asking the user for their name and vitural player's name...
user_name = input("\nPlease enter your name: ")
virtual_player = input("\nWhat should the name of virtual player be? ")


while True:
  
    print("\nChoose your strategy to win...\n")
    for key, value in choices.items():
        print(f"{key}. {value}")
    print("4. Exit 🚪")

    user_choice = input("\nEnter your choice: ")

    if user_choice == '4':
        print(f"\nThanks for playing! Goodbye {user_name} 👋")
        break

    computer_choice = random.choice(list(choices.values()))
    print(f"\nYou chose: {user_choice}")
    print(f"{virtual_player} chose: {computer_choice}")
    print(get_result(user_choice, computer_choice))
