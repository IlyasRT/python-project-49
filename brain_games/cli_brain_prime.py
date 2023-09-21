from random import randint
import prompt 
from brain_games.cli import welcome_user
print('brain-prime')
def brain_prime():
    name = welcome_user()
    count = 0
    correction_of_user_answer = True

    while count < 3:
        number = randint(1, 100)
        print(f'Question: {number}')
        list_of_dividers=[]
        for i in range(1,number+1):
            if number%i==0:
                list_of_dividers.append(i)
                
        print('Answer \"yes\" if given number is prime. Otherwise answer \"no\".')
        user_answer = prompt.string('Your answer: ').lower()
        if (user_answer == 'yes' and len(list_of_dividers)==2) or (user_answer == 'no' and len(list_of_dividers)>2):
            count += 1
            print(f'Correct!')
        else:
            correction_of_user_answer = False
            count += 3
            print(f'\'{user_answer}\' is wrong answer;(. Let\'s try again, {name}!')

            
            
    if correction_of_user_answer == True:
        print(f'Congratulations, {name}!')
