from random import randint
import prompt
from brain_games.games.cli import welcome_user
from brain_games.games.constants import NUMBER_OF_REPETITIONS
print('brain-prime')


def brain_prime():
    name = welcome_user()
    count = 0
    correction_of_user_answer = True
    while count < NUMBER_OF_REPETITIONS:
        number = randint(1, 100)
        print(f'Question: {number}')
        d = []
        for i in range(1, number + 1):
            if number % i == 0:
                d.append(i)
        print('Answer \"yes\" if given number is prime.Otherwise answer \"no\".')
        an = prompt.string('Your answer: ').lower()
        if an == 'yes' and len(d) == 2:
            count += 1
            print('Correct!')

        elif an == 'no' and len(d) > 2:
            count += 1
            print('Correct!')
            
        elif an == 'yes' and len(d) > 2:
            correction_of_user_answer = False
            count += 3
            print(f'\'{an}\' is wrong answer;(.Correct answer was \'no\'.')
            print(f'Let\'s try again, {name}!')
            
        elif an == 'no' and len(d) == 2:
            correction_of_user_answer = False
            count += 3
            print(f'\'{an}\' is wrong answer;(.Correct answer was \'yes\'.')
            print(f'Let\'s try again, {name}!')    
        
    if correction_of_user_answer is True:
        print(f'Congratulations, {name}!')
