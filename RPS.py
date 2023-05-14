import random


def play():
    user = input("Whats your choice? 'r' for Rock 's' for Scissors 'p' for paper\n")
    computer = random.choice(['r', 's', 'p'])

    if user == computer:
        return 'Its a tie'

    if is_win(user, computer):
        return 'You Won!'

    return 'You Lost'


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
            or (player == 'p' and opponent == 'r'):
        return True


print(play())
