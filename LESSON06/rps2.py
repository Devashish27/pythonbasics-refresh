
import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playagain = True

while playagain:

    # print(RPS(2))
    # print(RPS.ROCK)
    # print(RPS['ROCK'])
    # print(RPS.ROCK.value)
    # sys.exit()

    playerchoice = input(
        "\nEnter...\n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")

    player = int(playerchoice)

    if player < 1 | player > 3:
        sys.exit("You must enter 1, 2 or 3.")

    computerchoice = random.choice("123")

    computer = int(computerchoice)
    # You are again casting into int
    # which is same as above

    print("\nYou chose" + str(RPS(player)).replace('RPS.', '') + ".")
    print("PC chose" + str(RPS(computer)).replace('RPS.', '') + ".\n")

    if player == 1 and computer == 3:
        print("🥳 You win!")
    elif player == 2 and computer == 1:
        print("🥳 You win!")
    elif player == 3 and computer == 2:
        print("🥳 You win!")
    elif player == computer:
        print("🥱 Draw")
    else:
        print("😎 PC wins!")

    playagain = input("\nPlay again? \nY for Yes or \nQ for Quit: \n\n")

    if playagain.lower() == "y":
        continue
    else:
        print("\n🥂🥂🥂🥂🥂")
        print("Thank you for playing!!\n")
        playagain = False
        # break can also be used.

sys.exit("Bye! 👋👋")
