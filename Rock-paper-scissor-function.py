import random

import computer as computer

print("Welcome to the Game HUMAN.....")

def play():
    human = input("r for Rock\n" "s for Scissors\n" "p for Paper\n" "What is your Choice : ")
    human = human.lower()

    computer = random.choice(['r', 's', 'p'])

    if human == computer:
        return "You and computer both have chosen {}. It's a Tie".format(computer)

    if is_win(human, computer):
        return "You have chosen {} and the computer has chosen {}. You won!".format(human, computer)

    return "You have chosen {} and the computer had chosen {}. You lost!".format(human, computer)

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False


print(play())