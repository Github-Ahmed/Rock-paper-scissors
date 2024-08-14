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

game_images = [rock, paper, scissors]

player = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player >= 3 or player < 0:
    print("You typed an invalid number, you lose!")

else:
    print(game_images[player])
    comp = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[comp])

    if player == 0 and comp == 2:
        print("You win!")
    elif comp == 0 and player == 2:
        print("You lose!")
    elif comp > player:
        print("You lose!")
    elif player > comp:
        print("You win!")
    elif comp == player:
        print("It's a draw")