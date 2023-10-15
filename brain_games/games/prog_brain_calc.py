from random import randint
DESCR = 'What is the result of the expression?'
LOWER_BOUND = 1
UPPER_BOUND = 10
LOWER_BOUND_ACTION = 0
UPPER_BOUND_ACTION = 2


def get_example_and_answer():
    FIRST_NUMBER_EXAMPLE = randint(LOWER_BOUND, UPPER_BOUND)
    SECOND_NUMBER_EXAMPLE = randint(LOWER_BOUND, UPPER_BOUND)
    list_of_action = ['+', '-', '*']
    random_action = randint(LOWER_BOUND_ACTION, UPPER_BOUND_ACTION)
    action = list_of_action[random_action]
    summ = FIRST_NUMBER_EXAMPLE + SECOND_NUMBER_EXAMPLE
    delta = FIRST_NUMBER_EXAMPLE - SECOND_NUMBER_EXAMPLE
    multi = FIRST_NUMBER_EXAMPLE * SECOND_NUMBER_EXAMPLE
    list_of_calculation = [summ, delta, multi]
    match action:
        case '+':
            answ = str(list_of_calculation[random_action])
            question = (f'{FIRST_NUMBER_EXAMPLE} {action}'
                        f' {SECOND_NUMBER_EXAMPLE}')
            return question, answ
        case '-':
            answ = str(list_of_calculation[random_action])
            question = (f'{FIRST_NUMBER_EXAMPLE} {action}'
                        f' {SECOND_NUMBER_EXAMPLE}')
            return question, answ
        case '*':
            answ = str(list_of_calculation[random_action])
            question = (f'{FIRST_NUMBER_EXAMPLE} {action}'
                        f' {SECOND_NUMBER_EXAMPLE}')
            return question, answ
