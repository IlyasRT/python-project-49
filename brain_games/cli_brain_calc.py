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
        action = ['+','-','*']
        action_index = randint(0, 2)
        summ = a + b
        delta = a - b
        multi = a * b
        action_table=[summ,delta,multi]
        
        print('What is the result of the expression?')
        print(f'Question: {a} {action[action_index]} {b}')
        user_answer = int(prompt.string('Your answer:'))
        if user_answer == action_table[action_index]:
            count += 1
            print(f'Correct!')
        else:
            correction_of_user_answer = False
            count += 3
            print(f'\'{user_answer}\' is wrong answer;(.Correct answer was \'{action_table[action_index]}\'. Let\'s try again, {name}!')
    if correction_of_user_answer == True:
        print(f'Congratulations, {name}!')
