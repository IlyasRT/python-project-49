from random import randint
DESCR = 'Answer \"yes\" if given number is prime. Otherwise answer \"no\".'
LOWER_BOUND = 2
UPPER_BOUND = 30


def get_example_and_answer():
    NUMBER_EXAMPLE = randint(LOWER_BOUND, UPPER_BOUND)
    question = NUMBER_EXAMPLE
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
