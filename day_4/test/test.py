import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if 0> user_choice or user_choice > 2:
    user_choice = int(input("Wrong number. between 0 to 2\n"))


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


choice_list=[rock,paper,scissors]
random_number=random.randint(0,2)

print(f"{choice_list[user_choice]}\nComputer chose:\n{choice_list[random_number]}\n")

if user_choice == random_number:
    print("It’s a draw.")
elif (user_choice - random_number) % 3 == 1:
    print("You win.")
else:
    print("You lose.")