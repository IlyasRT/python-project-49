from random import randint
print('brain-progression')
DESCR = 'Answer \"yes\" if given number is prime. Otherwise answer \"no\".'


def initial_data():
    number = randint(2, 30)
    print(f'Question: {number}')
    d = []
    for i in range(1, number + 1):
        if number % i == 0:
            d.append(i)

    if len(d) == 2:
        answ = 'yes'
        return answ
    else:
        answ = 'no'
        return answ
