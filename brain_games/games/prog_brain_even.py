from random import randint
print('brain-even')
DESCR = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_example_and_answer():
    expression = randint(1, 10)
    if check_even(expression) is True:
        answ = 'yes'
    else:
        answ = 'no'
    return expression, answ


def check_even(x):
    if int(x % 2) == 0:
        answer = True
    elif int(x % 2) != 0:
        answer = False
    return answer
