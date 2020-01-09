from random import choice
import sys

# Testing upstream

player_wins = 0
computer_wins = 0
winning_score = 3
choice_list = ['rock', 'paper', 'scissors']

print('Welcome to Rock Paper Scissors IQ OVER 9000')
print(f'Score {winning_score} points to win. Enter "quit" to exit. GOOD LUCK!')

while player_wins < winning_score and computer_wins < winning_score:
    human = input('Please enter your choice: ').casefold()
    if human == 'q' or human == 'quit':
        sys.exit('Thank you for playing!')
    elif human not in choice_list:
        print('Please enter rock, paper or scissors')
        continue

    pc = choice(choice_list)
    print('Computer chose ' + pc)

    if pc == human:
        print("Shoot, it's a tie!")
    elif (pc == 'rock' and human == 'scissors') or (pc == 'paper' and human == 'rock') or (
            pc == 'scissors' and human == 'paper'):
        print('Oh no, computer outsmarted you!')
        computer_wins += 1
    else:
        print('You won big brain!')
        player_wins += 1

    print(f'Player: {player_wins} Computer: {computer_wins}')
    pc = None

if player_wins > computer_wins:
    print('Congratulations, you won!')
else:
    print('Oh no, you lost!')
print(f'FINAL SCORE Player: {player_wins} Computer: {computer_wins}')
