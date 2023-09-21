from random import randint
import prompt
from brain_games.games.cli import welcome_user
from brain_games.games.constants import NUMBER_OF_REPETITIONS

print('brain_calc')


def brain_calc():
    name = welcome_user()
    count = 0
    correction_of_user_answer = True

    while count < NUMBER_OF_REPETITIONS:
        a = randint(1, 10)
        b = randint(1, 10)
        action = ['+', '-', '*']
        index = randint(0, 2)
        summ = a + b
        delta = a - b
        multi = a * b
        act = [summ, delta, multi]
        print('What is the result of the expression?')
        print(f'Question: {a} {action[index]} {b}')
        user_answer = int(prompt.string('Your answer: '))
        if user_answer == act[index]:
            count += 1
            print('Correct!')
        else:
            correction_of_user_answer = False
            count += 3
            print(f'\'{user_answer}\' is wrong answer;(.Correct answer was \'{act[index]}\'.')
            print(f'Let\'s try again, {name}!')
    if correction_of_user_answer is True:
        print(f'Congratulations, {name}!')
