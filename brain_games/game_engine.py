import prompt
NUMBER_OF_ROUNDS = 3


def run_game_process(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCR)
    count = 0
    correction_of_user_answer = True
    while count < NUMBER_OF_ROUNDS:
        question, answ = game.get_example_and_answer()
        print('Question:', question)
        user_answer = prompt.string('Your answer: ')
        if user_answer == answ:
            print('Correct!')
            count += 1
        else:
            correction_of_user_answer = False
            print(f'\'{user_answer}\' is wrong answer;(.'
                  f'Correct answer was \'{answ}\'.')
            print(f'Let\'s try again, {name}!')
            count = 3
    if correction_of_user_answer is True:
        print(f'Congratulations, {name}!')
