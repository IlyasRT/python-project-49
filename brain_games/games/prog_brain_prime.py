from random import randint
print('brain-prime')
DESCR = 'Answer \"yes\" if given number is prime. Otherwise answer \"no\".'


def get_example_and_answer():
    expression = randint(2, 30)
    if check_prime(expression) is True:
        answ = 'yes'
    else:
        answ = 'no'
    return expression, answ


def check_prime(x):
    d = []
    for i in range(1, x + 1):
        if x % i == 0:
            d.append(i)
    if len(d) == 2:
        answer = True
        return answer
    else:
        answer = False
        return answer
