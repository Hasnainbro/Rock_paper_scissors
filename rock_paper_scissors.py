import random

# Emojis representing the game choices
rock = "✊"
paper = "🖐"
scissors = "✌️"

# Create a list of choices
choice = [rock, paper, scissors]

# Get the user's input (0 for Rock, 1 for Paper, 2 for Scissors)
user_input = int(input("Choose between 0 for Rock, 1 for Paper, and 2 for Scissors: "))

# Display the user's choice
print("You chose: ")
print(choice[user_input])

# Generate a random choice for the computer (0 for Rock, 1 for Paper, 2 for Scissors)
computer_choose = random.randint(0, 2)

# Display the computer's choice
print(f"Computer chose:")
print(choice[computer_choose])

# Compare the user's choice with the computer's choice to determine the winner
if user_input >= 3 or user_input < 0:
    print("Invalid Choice!")
elif user_input == 0 and computer_choose == 2:
    print("You Win")
elif computer_choose == 0 and user_input == 2:
    print("Computer Wins")
elif user_input > computer_choose:
    print("You Win")
elif computer_choose > user_input:
    print("Computer Wins")
elif user_input == computer_choose:
    print("It's a Draw")
else:
    print("Invalid Input")
