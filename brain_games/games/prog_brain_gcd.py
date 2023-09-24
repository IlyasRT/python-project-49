from random import randint
print('brain-gcd')
DESCR = 'Find the greatest common divisor of given numbers.'


def initial_data():
    a, b = randint(1, 10), randint(1, 10)
    list_of_number = [a, b]
    list_of_dividers = []
    min_number = min(list_of_number)
    for i in range(1, min_number + 1):
        if a % i == 0 and b % i == 0:
            list_of_dividers.append(i)
            d = max(list_of_dividers)
    print(f'Question: {a} {b}')
    answ = str(d)
    return answ
