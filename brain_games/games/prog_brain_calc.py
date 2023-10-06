from random import randint

print('brain-calc')
DESCR = 'What is the result of the expression?'


def get_example_and_answer():
    number_1 = randint(1, 10)
    number_2 = randint(1, 10)
    list_of_action = ['+', '-', '*']
    i = randint(0, 2)
    action = list_of_action[i]
    summ = number_1 + number_2
    delta = number_1 - number_2
    multi = number_1 * number_2
    list_of_calculation = [summ, delta, multi]
    match action:
        case '+':
            answ = str(list_of_calculation[i])
            expression = f'{number_1} {action} {number_2}'
            return expression, answ
        case '-':
            answ = str(list_of_calculation[i])
            expression = f'{number_1} {action} {number_2}'
            return expression, answ
        case '*':
            answ = str(list_of_calculation[i])
            expression = f'{number_1} {action} {number_2}'
            return expression, answ
