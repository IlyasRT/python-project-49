from random import randint
import prompt 
from brain_games.cli import welcome_user
print(f'brain-gcd')
def brain_gcd():
    name = welcome_user()
    count = 0
    correction_of_user_answer = True
    while count < 3:
        a,b = randint(1, 20),randint(1, 20)
        list_of_number = [a, b]
        list_of_dividers = []
        min_number = min(list_of_number)
        for i in range(1, min_number+1):
            if a % i == 0 and b % i == 0:
                list_of_dividers.append(i)
                max_divider = max(list_of_dividers)
        print(f'Find the greatest common divisor of given numbers.')
        correction_of_user_answer = True
        print(f'Question: {a} {b}')
        user_answer = prompt.string('Your answer:')
        if int(user_answer) == max_divider:
            #print(f'вошли user_answer == max_divider')
            count += 1
            print(f'Correct!')
        else:
            count = 3
            correction_of_user_answer = False
            print(f'\'{user_answer}\' is wrong answer;(.Correct answer was \'{max_divider}\'. Let\'s try again, {name}!')
    if correction_of_user_answer == True:
        print(f'Congratulations, {name}!')
