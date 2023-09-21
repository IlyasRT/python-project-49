from random import randint
import prompt
from brain_games.games.cli import welcome_user
from brain_games.games.constants import NUMBER_OF_REPETITIONS
print('brain-prog')


def brain_prog():
    name = welcome_user()
    correction_of_user_answer = True
    count = 0
    while count < NUMBER_OF_REPETITIONS:
        length_of_progression = randint(5, 10)
        position_of_unknown_element = randint(0, length_of_progression-1)
        delta_of_progression = randint(1, 10)
        x = length_of_progression*delta_of_progression+1
        progression = []
        for i in range(delta_of_progression, x, delta_of_progression):
            progression.append(i)
        unknown_element = progression[position_of_unknown_element]
        progression[position_of_unknown_element] = '..'
        print('What number is missing in the progression?')
        correction_of_user_answer = True
        print('Question: ', end = '')
        print(*progression)
        user_answer = prompt.string('Your answer: ')
        if int(user_answer) == unknown_element:
            count += 1
            print('Correct!')
        else:
            count = 3
            correction_of_user_answer = False
            print(f'\'{user_answer}\' is wrong answer;(. Correct answer was \'{unknown_element}\'.')
            print(f'Let\'s try again, {name}!')
    if correction_of_user_answer is True:
        print(f'Congratulations, {name}!')
