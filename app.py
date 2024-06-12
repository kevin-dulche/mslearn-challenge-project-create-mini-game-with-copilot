options = ['paper', 'rock', 'scissors']

player_wins = 0
computer_wins = 0
rounds = 0

import random

def get_computer_choice():
    return random.choice(options)

def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'draw'
    if player_choice == 'rock':
        return 'player' if computer_choice == 'scissors' else 'computer'
    if player_choice == 'paper':
        return 'player' if computer_choice == 'rock' else 'computer'
    if player_choice == 'scissors':
        return 'player' if computer_choice == 'paper' else 'computer'

def play(player_choice):
    computer_choice = get_computer_choice()
    winner = get_winner(player_choice, computer_choice)
    if winner == 'player':
        global player_wins
        player_wins += 1
    elif winner == 'computer':
        global computer_wins
        computer_wins += 1
    return {
        'player_choice': player_choice,
        'computer_choice': computer_choice,
        'winner': winner
    }

while True:

    player_choice = input('Enter your choice: ')
    if player_choice == 'exit':
        print(f'Player wins: {player_wins}')
        print(f'Computer wins: {computer_wins}')
        print(f'Rounds played: {rounds}')
        break
    if player_choice not in options:
        print('Invalid choice')
        continue
    rounds += 1
    result = play(player_choice)
    print(f'Player choice: {result["player_choice"]}')
    print(f'Computer choice: {result["computer_choice"]}')
    print(f'Winner: {result["winner"]}')