from random import randint
import prompt
from brain_games.games.constants import NUMBER_OF_REPETITIONS
    
    
    
    
    
def start_game(x):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(x.DESCRIPTION_OF_GAME)
    return name
    
def congratulations():
    name='ILyas' # не получается импортировать из start_game
    
    print(f'Congratulations, {name}!')

