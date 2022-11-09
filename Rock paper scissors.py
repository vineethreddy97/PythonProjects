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
game_images=[rock,paper,scissors]
user_number=int(input("What do you choose ? Type 0 for Rock , 1 for paper or 2 for Scissors\n"))
if user_number>=3 or user_number<0:
    print("The number is invalid you loose")
else:
    print(game_images[user_number])
    print("Computer chose:")
    computer_chose=random.randint(0,2)
    print(game_images[computer_chose])
    if user_number==0 and computer_chose==2:
        print("You Wins")
    elif computer_chose==0 and user_number==2:
        print("You loose")
    elif user_number > computer_chose:
        print("You loose")
    elif computer_chose>user_number:
        print("You win")
    elif user_number==computer_chose:
        print("Its Draw")