from random import randint
import prompt
from brain_games.games.cli import welcome_user
from brain_games.games.constants import NUMBER_OF_REPETITIONS
print('brain-gcd')


def brain_gcd():
    name = welcome_user()
    count = 0
    correction_of_user_answer = True
    while count < NUMBER_OF_REPETITIONS:
        a, b = randint(1, 20), randint(1, 20)
        list_of_number = [a, b]
        list_of_dividers = []
        min_number = min(list_of_number)
        for i in range(1, min_number + 1):
            if a % i == 0 and b % i == 0:
                list_of_dividers.append(i)
                d = max(list_of_dividers)
        print('Find the greatest common divisor of given numbers.')
        correction_of_user_answer = True
        print(f'Question: {a} {b}')
        n = prompt.string('Your answer: ')
        if int(n) == d:
            count += 1
            print('Correct!')
        else:
            count = 3
            correction_of_user_answer = False
            print(f'\'{n}\' is wrong answer;(.Correct answer was \'{d}\'.')
            print(f'Let\'s try again, {name}!')
    if correction_of_user_answer is True:
        print(f'Congratulations, {name}!')
