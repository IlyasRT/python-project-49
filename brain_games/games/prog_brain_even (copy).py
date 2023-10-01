from random import randint
print('brain-even')
DESCR = 'Answer "yes" if the number is even, otherwise answer "no".'


def initial_data():
    random_number = randint(1, 10)
    print(f'Question: {random_number}')
    if int(random_number % 2) == 0:
        answ = 'yes'
        return answ
    elif int(random_number % 2) != 0:
        answ = 'no'
        return answ
