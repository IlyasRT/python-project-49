from random import randint
from brain_games.games.start import start_game
import prompt
from brain_games.games.start import congratulations
print('brain-calc')
DESCRIPTION_OF_GAME = 'What is the result of the expression?'


def brain_calc():
    count = 0
    correction_of_user_answer = True
    while count < 1:
        a = randint(1, 10)
        b = randint(1, 10)
        y = ['+', '-', '*']
        i = randint(0, 2)
        summ = a + b
        delta = a - b
        multi = a * b
        t = [summ, delta, multi]
        print(f'Question: {a} {y[i]} {b}')
        an = int(prompt.string('Your answer: '))
        if an == t[i]:
            count += 1
            print('Correct!')
        else:
            #name = start_game() # не работает
            #name = start_game(prog_brain_calc) # не работает
            name='Ilyas' # ввел, проверить работу целиком
            correction_of_user_answer = False
            count += 3
            
            print(f'\'{an}\' is wrong answer;(. Correct answer was \'{t[i]}\'.')
            print(f'Let\'s try again, {name}!')
    if correction_of_user_answer is True:
        print('зашли --> if correction_of_user_answer is True')
        congratulations()
