from random import randint
print('brain-even')
DESCRIPTION_OF_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def initial_data():
    random_number = randint(1, 10)
    print(f'Question: {random_number}')
    if int(random_number % 2) == 0:
        correct_answer = 'yes'
        return correct_answer
    elif int(random_number % 2) != 0:
        correct_answer = 'no'
        return correct_answer
