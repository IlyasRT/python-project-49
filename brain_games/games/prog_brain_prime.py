from random import randint
DESCR = 'Answer \"yes\" if given number is prime. Otherwise answer \"no\".'


def get_example_and_answer():
    question = randint(2, 30)
    if is_prime(question) is True:
        answ = 'yes'
    else:
        answ = 'no'
    return question, answ


def is_prime(x):
    list_of_dividers = []
    for i in range(1, x + 1):
        if x % i == 0:
            list_of_dividers.append(i)
    if len(list_of_dividers) == 2:
        answer = True
        return answer
    else:
        answer = False
        return answer
