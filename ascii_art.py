from pyfiglet import figlet_format as f
from termcolor import colored as c


def ascii_print():
    message = input('What message do you want to print? ')

    while True:
        try:
            colour = input('What colour? ')
            answer = c(f(message), colour)
            break
        except KeyError:
            print('Colour is not valid. Please choose from red, green, yellow, blue, magenta, cyan, white')
    return print(answer)


ascii_print()
