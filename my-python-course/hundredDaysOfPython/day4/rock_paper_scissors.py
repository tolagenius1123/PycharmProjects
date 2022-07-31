import random

rock = "🤜🤜🤜🤜🤜🤜🤜🤜🤜🤜🤜🤜🤜🤜🤜"
paper = "👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍"
scissors = "✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌"

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print(f"Computer choose: ")
print(game_images[computer_choice ])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You loose!")
if user_choice == 0 and  computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You loose!")
elif computer_choice > user_choice:
    print("You loose!")
elif user_choice > computer_choice:
    print("you win")
elif computer_choice == user_choice:
    print("It's a draw")
else:
    print("You typed an invalid number, you loose!")