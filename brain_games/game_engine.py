import prompt
NUMBER_OF_ROUNDS = 3


def game_engine_function(name_of_game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(name_of_game.DESCR)
    count = 0
    correction_of_user_answer = True
    while count < NUMBER_OF_ROUNDS:
        question, answ = name_of_game.get_example_and_answer()
        print('Question:', question)
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
