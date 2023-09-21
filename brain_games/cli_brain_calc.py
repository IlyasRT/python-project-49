from random import randint
import prompt
from brain_games.cli import welcome_user
print('brain_calc')


def brain_calc():
    name = welcome_user()
    count = 0
    correction_of_user_answer = True

    while count < 3:
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
