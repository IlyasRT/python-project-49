from random import randint

print('brain-calc')
DESCR = 'What is the result of the expression?'


def initial_data():
    a = randint(1, 10)
    b = randint(1, 10)
    list_of_action = ['+', '-', '*']
    i = randint(0, 2)
    action = list_of_action[i]
    summ = a + b
    delta = a - b
    multi = a * b
    list_of_calculation = [summ, delta, multi]
    match action:
        case '+':
            print(f'Question: {a} {action} {b}')
        case '-':
            print(f'Question: {a} {action} {b}')
        case '*':
            print(f'Question: {a} {action} {b}')
    answ = str(list_of_calculation[i])
    return answ
