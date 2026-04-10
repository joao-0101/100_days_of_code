import random

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

user_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

if user_input == "0":
    print(rock)
elif user_input == "1":
    print(paper)
elif user_input == "2":
    print(scissors)
else:
    print("Invalid Input")1

game = [rock, paper, scissors]
print("Computer chose:")
computer_choice = (print(random.choice(game)))

if user_input == computer_choice:
    print("Draw!")
elif user_input == rock and computer_choice == scissors:
    print("You win!")
elif user_input == paper and computer_choice == rock:
    print("You win!")
elif user_input == scissors and computer_choice == paper:
    print("You win!")
elif user_input == rock and computer_choice == paper:
    print("You lose!")
elif user_input == paper and computer_choice == scissors:
    print("You lose!")
else:
    print("You lose!")
