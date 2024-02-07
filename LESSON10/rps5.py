
import sys
import random
from enum import Enum


def rps():
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal computer_wins

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
            nonlocal player_wins
            nonlocal computer_wins

            if player == 1 and computer == 3:
                player_wins += 1
                return "🥳 You win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "🥳 You win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "🥳 You win!"
            elif player == computer:
                return "🥱 Draw"
            else:
                computer_wins += 1
                return "😎 PC wins!"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print("\nGame count: " + str(game_count))
        print("\nComputer Wins: " + str(computer_wins))
        print("\nPython Wins: " + str(player_wins))

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

    return play_rps


play = rps()

play()
