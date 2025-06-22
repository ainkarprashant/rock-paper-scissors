import random

# ASCII Art for Rock, Paper, Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Store choices in a list
choices = [rock, paper, scissors]

def get_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """Main function to play the game."""
    print("Welcome to Rock, Paper, Scissors!")
    print("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")

    try:
        user_choice = int(input("Your choice: "))
        if user_choice < 0 or user_choice > 2:
            print("Invalid input. You must enter 0, 1, or 2.")
            return

        print("\nYou chose:")
        print(choices[user_choice])

        # Computer's choice
        computer_choice = random.randint(0, 2)
        print("Computer chose:")
        print(choices[computer_choice])

        # Determine winner
        result = get_winner(user_choice, computer_choice)
        print(result)

    except ValueError:
        print("Invalid input. Please enter a number (0, 1, or 2).")

# Replay loop
while True:
    play_game()
    replay = input("Do you want to play again? (yes/no): ").strip().lower()
    if replay != 'yes':
        print("Thanks for playing! Goodbye!")
        break