from random import randint
from brain_games.games.start import start_game
import prompt

print('brain-calc')
DESCRIPTION_OF_GAME = 'What is the result of the expression?'


def initial_data():
        a = randint(1, 10)
        b = randint(1, 10)     
        list_of_action = ['+', '-', '*']
        i = randint(0, 2)
        action = list_of_action[i] 
        summ = a + b
        delta = a - b
        multi = a * b            
        list_of_calculation = [summ, delta, multi]
        match action:
            case '+':
                print(f'Question: {a} {action} {b}')
                
            case '-':
                print(f'Question: {a} {action} {b}')
                
            case '*':
                print(f'Question: {a} {action} {b}')          
        correct_answer = list_of_calculation[i]
        return correct_answer
