from random import randint
DESCR = 'Find the greatest common divisor of given numbers.'


def get_example_and_answer():
    FIRST_NUMBER_EXAMPLE = randint(1, 10)
    SECOND_NUMBER_EXAMPLE = randint(1, 10)
    question = f'{FIRST_NUMBER_EXAMPLE} {SECOND_NUMBER_EXAMPLE}'
    answ = str(check_gcd(FIRST_NUMBER_EXAMPLE, SECOND_NUMBER_EXAMPLE))
    return question, answ


def check_gcd(x, y):
    list_of_number = [x, y]
    list_of_dividers = []
    min_number = min(list_of_number)
    for i in range(1, min_number + 1):
        if x % i == 0 and y % i == 0:
            list_of_dividers.append(i)
    answer = max(list_of_dividers)
    return answer
