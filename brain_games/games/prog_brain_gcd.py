from random import randint
DESCR = 'Find the greatest common divisor of given numbers.'


def get_example_and_answer():
    a, b = randint(1, 10), randint(1, 10)
    question = f'{a} {b}'
    answ = str(check_gcd(a, b))
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
