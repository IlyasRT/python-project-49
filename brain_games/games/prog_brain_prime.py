from random import randint
import prompt
from brain_games.games.cli import welcome_user
from brain_games.games.constants import NUMBER_OF_REPETITIONS, A_YES, A_NO, A_CM

print('brain-prime')


def brain_prime():
    name = welcome_user()
    count = 0
    correction = True
    print('Answer \"yes\" if given number is prime. Otherwise answer \"no\".')
    while count < NUMBER_OF_REPETITIONS and correction is True:
        number = randint(1, 30)
        print(f'Question: {number}')
        d = []
        for i in range(1, number + 1):
            if number % i == 0:
                d.append(i)
        an = prompt.string('Your answer: ')
        if len(d) == 2:
            var = 2
        else:
            var = 3
        ans = (an, var)
        match ans:
            case 'yes', 2:
                count += 1
                print('Correct!')
            case 'no', 3:
                count += 1
                print('Correct!')
            case 'no', 2:
                correction = False
                print(f'{A_NO}\n{A_CM}{name}!')
            case 'yes', 3:
                correction = False
                print(f'{A_YES}\n{A_CM}{name}!')
    if correction is True:
        print(f'Congratulations, {name}!')
