from random import choice
import sys

choice_list = ['rock', 'paper', 'scisors']
pc = choice(choice_list)

print('Welcome to Rock Paper Scisors SMARTER')
human = input('Please enter your choice: ').casefold()
if human == "" or human not in choice_list:
    sys.exit('Please enter rock, paper or scisors')
    
print('Computer chose ' + pc)

if pc == human:
    print("Shoot, it's a tie!")
elif (pc == 'rock' and human == 'scisors') or (pc == 'paper' and human == 'rock') or (pc == 'scisors' and human == 'paper'):
    print('Oh no, computer outsmarted you!')
else:
    print('You won big brain!')
