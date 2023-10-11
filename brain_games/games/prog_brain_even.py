from random import randint
DESCR = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_example_and_answer():
    NUMBER_EXAMPLE = randint(1, 10)
    question = NUMBER_EXAMPLE
    if is_even(question) is True:
        answ = 'yes'
    else:
        answ = 'no'
    return question, answ


def is_even(x):
    if int(x % 2) == 0:
        answer = True
    elif int(x % 2) != 0:
        answer = False
    return answer
