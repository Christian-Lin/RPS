"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random

import os

os.system("")

moves = ['rock', 'paper', 'scissors', 'spock', 'lizard']

playersText = """
  Rock, Paper, Scissors, Spock, Lizard!

  Rules of the game:
  - Rock beats Scissors and Lizard.
  - Paper beats Rock and Spock.
  - Scissors beats Paper and Lizard.
  - Lizard beats Spock and Paper.
  - Spock beats Scissors and Rock.

  You will play against one of the following opponents:
  Spock: always chooses Spock.
  Random: chooses moves randomly.
  ReflectPlayer: copies the opponent's previous move.
  Cycler: cycles through rock, paper, scissors, Spock, and lizard.
  """


class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


class Player:
    """
    The Player class is the parent class for all of the Players
    in this game
    """
    def __init__(self):
        self.prev_move1 = ""
        self.prev_move2 = ""

    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        self.prev_move1 = my_move
        self.prev_move2 = their_move


class Random(Player):
    def move(self):
        return random.choice(moves)


class Spock(Player):
    def move(self):
        return 'spock'


class Human(Player):
    def move(self):
        hmove = input(f"{style.RED}What's your move? {style.RESET}").lower()
        while hmove not in moves:
            hmove = input(f"Please choose between {moves[0]}, {moves[1]}, "
                          f"{moves[2]}, {moves[3]}, and {moves[4]}: ").lower()
        return hmove


class ReflectPlayer(Player):
    def move(self):
        if self.prev_move2 == 'rock':
            return 'rock'
        elif self.prev_move2 == 'paper':
            return 'paper'
        elif self.prev_move2 == 'spock':
            return 'spock'
        elif self.prev_move2 == 'lizard':
            return 'lizard'
        else:
            return 'scissors'


class Cycler(Player):
    def move(self):
        if self.prev_move1 == 'rock':
            return moves[1]   # paper
        elif self.prev_move1 == 'paper':
            return moves[2]   # scissors
        elif self.prev_move1 == 'scissors':
            return moves[3]   # spock
        elif self.prev_move1 == 'spock':
            return moves[4]   # lizard
        else:
            return moves[0]   # rock


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = ""
        self.score2 = ""

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"{style.RED}Player 1: {move1}{style.RESET} -- "
              f"{style.BLUE}Player 2: {move2}{style.RESET}")
        self.beats(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def beats(self, move1, move2):
        if move1 == move2:
            print(style.YELLOW+"Tie!"+style.RESET)
            print(f"{style.GREEN}{self.score1} to "
                  f"{self.score2}{style.RESET}\n")
        elif ((move1 == 'rock' and move2 == 'scissors') or
                (move1 == 'rock' and move2 == 'lizard') or
                (move1 == 'scissors' and move2 == 'paper') or
                (move1 == 'scissors' and move2 == 'lizard') or
                (move1 == 'paper' and move2 == 'rock') or
                (move1 == 'paper' and move2 == 'spock') or
                (move1 == 'spock' and move2 == 'scissors') or
                (move1 == 'spock' and move2 == 'rock') or
                (move1 == 'lizard' and move2 == 'paper') or
                (move1 == 'lizard' and move2 == 'spock')):
            print(style.RED+"Player 1 wins this round!"+style.RESET)
            self.score1 += 1
            print(f"{style.GREEN}{self.score1} to "
                  f"{self.score2}{style.RESET}\n")
        else:
            print(style.BLUE+"Player 2 wins this round!"+style.RESET)
            self.score2 += 1
            print(f"{style.GREEN}{self.score1} to "
                  f"{self.score2}{style.RESET}\n")

    def winner(self):
        if self.score1 == self.score2:
            print(f"{style.YELLOW}It's a tie! {self.score1} "
                  f"to {self.score2}!{style.RESET}")
        elif (self.score1 > self.score2):
            print(f"{style.RED}Player 1 wins the match! {self.score1} "
                  f"to {self.score2}!{style.RESET}")
        else:
            print(f"{style.BLUE}Player 2 wins the match! {self.score1} "
                  f"to {self.score2}!{style.RESET}")

    def play_again(self):
        repeat = input("Would you like to play again? (y/n)\n").lower()
        if repeat in ["y", "yes"]:
            players = [Spock(), Random(), ReflectPlayer(), Cycler()]
            self = Game(Human(), random.choice(players))
            self.play_game()
        elif repeat in ["n", "no"]:
            print("Thank you for playing. "
                  "See you next time!")
        else:
            print("Please type in 'y'(yes) or 'n'(no).")
            self.play_again()

    def play_game(self):
        self.score1 = 0
        self.score2 = 0
        rounds = input('How many rounds would you like to play? '
                       '(Maximum of 100)\n')
        r = range(1, 101)
        if rounds in str([*r]) and rounds != '0':
            print("Game start!\n")
            for round in range(1, int(rounds)+1):
                print(f"Round {round}:")
                self.play_round()
            self.winner()
            self.play_again()
        else:
            game.play_game()


if __name__ == '__main__':
    players = [Spock(), Random(), ReflectPlayer(), Cycler()]
    print(style.MAGENTA+playersText+style.RESET)
    game = Game(Human(), random.choice(players))
    game.play_game()
