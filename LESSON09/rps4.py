
import sys
import random
from enum import Enum

game_count = 0


def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    # playagain = True

    # while playagain:

        # print(RPS(2))
        # print(RPS.ROCK)
        # print(RPS['ROCK'])
        # print(RPS.ROCK.value)
        # sys.exit()

    playerchoice = input(
        "\nEnter...\n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")

    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1, 2 or 3.")
        return play_rps()

    player = int(playerchoice)

    # if player < 1 | player > 3:
    #     sys.exit()

    computerchoice = random.choice("123")

    computer = int(computerchoice)
    # You are again casting into int
    # which is same as above

    print("\nYou chose " + str(RPS(player)).replace('RPS.', '') .title() + ".")
    print("PC chose " + str(RPS(computer)).replace('RPS.', '').title() + ".\n")

    def decide_winner(player, computer):
        if player == 1 and computer == 3:
            return "🥳 You win!"
        elif player == 2 and computer == 1:
            return "🥳 You win!"
        elif player == 3 and computer == 2:
            return "🥳 You win!"
        elif player == computer:
            return "🥱 Draw"
        else:
            return "😎 PC wins!"

    game_result = decide_winner(player, computer)

    print(game_result)

    global game_count
    game_count += 1

    print("\nGame count: " + str(game_count))

    print("\nPlay Again?")

    while True:
        playagain = input("\nY for Yes or \nQ for Quit\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        # continue
        return play_rps
    else:
        print("\n🥂🥂🥂🥂🥂")
        print("Thank you for playing!!\n")
        # playagain = False
        # break can also be used.
        sys.exit("Bye! 👋👋")


play_rps()
