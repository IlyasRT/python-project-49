from random import randint
DESCR = 'What is the result of the expression?'



def get_example_and_answer():
    FIRST_NUMBER_OF_EXAMPLE = randint(1, 10)
    SECOND_NUMBER_OF_EXAMPLE = randint(1, 10)
    list_of_action = ['+', '-', '*']
    random_action = randint(0, 2)
    action = list_of_action[random_action]
    summ = FIRST_NUMBER_OF_EXAMPLE + SECOND_NUMBER_OF_EXAMPLE
    delta = FIRST_NUMBER_OF_EXAMPLE - SECOND_NUMBER_OF_EXAMPLE
    multi = FIRST_NUMBER_OF_EXAMPLE * SECOND_NUMBER_OF_EXAMPLE
    list_of_calculation = [summ, delta, multi]
    match action:
        case '+':
            answ = str(list_of_calculation[random_action])
            question = (f'{FIRST_NUMBER_OF_EXAMPLE} {action}'
                        f' {SECOND_NUMBER_OF_EXAMPLE}')
            return question, answ
        case '-':
            answ = str(list_of_calculation[random_action])
            question = (f'{FIRST_NUMBER_OF_EXAMPLE} {action}'
                        f' {SECOND_NUMBER_OF_EXAMPLE}')
            return question, answ
        case '*':
            answ = str(list_of_calculation[random_action])
            question = (f'{FIRST_NUMBER_OF_EXAMPLE} {action}'
                        f' {SECOND_NUMBER_OF_EXAMPLE}')
            return question, answ
