
import sys
import random
from enum import Enum


def rps():
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def play_rps(name):
        # nonlocal name
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
            f"\n{name}, please enter...\n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2 or 3.")
            return play_rps()

        player = int(playerchoice)

        # if player < 1 | player > 3:
        #     sys.exit()

        computerchoice = random.choice("123")

        computer = int(computerchoice)
        # You are again casting into int
        # which is same as above

        print(
            f"\n{name}, you chose {str(RPS(player)).replace('RPS.', '') .title()}.")
        print(f"PC chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal computer_wins

            if player == 1 and computer == 3:
                player_wins += 1
                return f"🥳 {name}, you win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🥳 {name}, you win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🥳 {name}, you win!"
            elif player == computer:
                return "🥱 Draw"
            else:
                computer_wins += 1
                return f"🐍 PC wins!\nSorry, {name}...😔"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s Wins: {player_wins}")
        print(f"\nPython Wins: {computer_wins}")

        print(f"\nPlay Again, {name}?")

        while True:
            playagain = input("\nY for Yes or \nQ for Quit\n")
            if playagain.lower() in ["y", "q"]:
                break

        if playagain.lower() == "y":
            return play_rps(name)
        else:
            print("\n🥂🥂🥂🥂🥂")
            print("Thank you for playing!!\n")
            # playagain = False
            # break can also be used.
            sys.exit(f"Bye {name}! 👋👋")

    return play_rps

# play()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Rock, Paper, Scissors game.')
    parser.add_argument('-n', '--name', type=str,
                        help='Your name', required=True)
    args = parser.parse_args()

    rock_paper_scissors = rps()
    rock_paper_scissors(args.name)
