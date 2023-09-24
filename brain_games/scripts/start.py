from random import randint
import prompt
from brain_games.games.constants import NUMBER_OF_REPETITIONS

    
def start_game(x):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(x.DESCRIPTION_OF_GAME)
    count = 0
    correction_of_user_answer = True
    
    while count < NUMBER_OF_REPETITIONS:
        correct_answer = x.initial_data()
        u_a = prompt.string('Your answer: ')
        
        if u_a == correct_answer:
            #print(f'{u_a} = {correct_answer}')
            
            print('Correct!')
            count += 1            
        else:
            #print(f'{u_a} != {correct_answer}')
            correction_of_user_answer = False
            print(f'\'{u_a}\' is wrong answer;(. Correct answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {name}!')
            count = 3
    if correction_of_user_answer is True:
        print(f'Congratulations, {name}!')
