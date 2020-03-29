from pyfiglet import figlet_format as f
from termcolor import colored as c
import requests
from random import choice

print(c(f('Dad Joke Generator'), 'blue'))
print('Run out of dad jokes? No problem!')

while True:

    topic = input('Give me a topic: ')

    url = 'https://icanhazdadjoke.com/search'
    response = requests.get(url,
                            headers={'Accept': 'application/json'},
                            params={'term': topic}
                            ).json()
    allJokes = response['results']
    numberOfJokes = response['total_jokes']

    if numberOfJokes == 1:
        print(f"I've got one joke about {topic} for you. Here it is: ")
        print(choice(allJokes)['joke'])
    elif numberOfJokes > 1:
        print(f"I've got {numberOfJokes} jokes about {topic} for you. Here is one: ")
        print(choice(allJokes)['joke'])
        con = input('Would you like to try another topic? y/n ')
        if con == 'n':
            break
    else:
        print(f"Sorry, I have no jokes about {topic}. Please try different topic.")





