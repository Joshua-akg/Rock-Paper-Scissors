import random

def main():
    #the computer and user can pick one of rock, paper or scissors
    computer = random.choice(['r', 'p','s'])
    user = ''

    #error check to ensure the user picks one of the three options
    while (user != 'r') and (user != 'p') and (user != 's'):
        user = input("Choose an option ['r' for rock, 'p' for paper or 's' for scissors]: ")

    if user == computer:
        return '\nIt\'s a DRAW!'

    if youWin(user, computer):
        return '\nYou WIN!'

    return '\nYou LOSE!'

def youWin(user, computer):
    #rules: r > s, s > p, p > r
    #returns true if by the rules, the user's choice trumps the computers

    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True    

print(main())
