from random import randint
import prompt
from brain_games.games.cli import welcome_user
from brain_games.games.constants import NUMBER_OF_REPETITIONS
print('brain_even')


def brain_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    correction_of_user_answer = True
    while count < NUMBER_OF_REPETITIONS:
        random_number = randint(1, 10)
        print(f'Question: {random_number}')
        user_answer = prompt.string('Your answer: ').lower()
        if (random_number % 2 == 0 and user_answer == 'yes'.lower()) or (
                random_number % 2 != 0 and user_answer == 'no'.lower()):
            count += 1
            print('Correct!')

        else:
            count = 3
            correction_of_user_answer = False
            print('\'yes\' is wrong answer ;\\(. Correct answer was \'no\'.')
            print(f'Let\'s try again, {name}!')
    if correction_of_user_answer is True:
        print(f'Congratulations, {name}!')
