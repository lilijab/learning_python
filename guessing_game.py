import random

random_number = random.randint(1,10)

while True:
    guess = int(input('Guess the number between 1 and 10: '))
    if guess > random_number:
        print('Too high, try again')
    elif guess < random_number:
        print('Too low, try again')
    else:
        print('Congratulations, you guessed it!')
        cont = input('Would you like to play again? y/n: ').lower()
        if cont == 'n':
            print('Thank you for playing!')
            break
        random_number = random.randint(1,10)