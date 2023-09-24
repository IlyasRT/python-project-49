import prompt
from brain_games.games.constants import NUMBER_OF_REPETITIONS


def start_game(x):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(x.DESCR_GAME)
    count = 0
    correction_of_user_answer = True
    while count < NUMBER_OF_REPETITIONS:
        answ = x.initial_data()
        u_a = prompt.string('Your answer: ')
        if u_a == answ:
            print('Correct!')
            count += 1
        else:
            correction_of_user_answer = False
            print(f'\'{u_a}\' is wrong answer;(.Correct answer was \'{answ}\'.')
            print(f'Let\'s try again, {name}!')
            count = 3
    if correction_of_user_answer is True:
        print(f'Congratulations, {name}!')
