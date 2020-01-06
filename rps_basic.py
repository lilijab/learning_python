print('Welcome to Rock Paper Scisors BASIC')
player1 = input('Player 1, please imput your choice: ')
print('*NO CHEATING*\n\n' * 25)
player2 = input('Player 2, please enter your choice: ')
if ((player1 == 'rock' or player1 == 'paper' or player1 == 'scisors') and (player2 == 'rock' or player2  == 'paper' or player2 == 'scisors')):
    if (player1 == player2):
        print("Shoot, it's a tie!")
    elif (player1 == 'rock' and player2 == 'scisors') or (player1 == 'scisors' and player2 == 'paper') or (player1 == 'paper' and player2 == 'rock'):
        print('Congratulations Player1, you won!')
    else:
        print('Congratulations Player2, you won!')
else:
    print('Please enter rock, paper or scisors')