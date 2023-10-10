from random import randint
DESCR = 'What is the result of the expression?'


def get_example_and_answer():
    first_number_of_example = randint(1, 10)
    second_number_of_example = randint(1, 10)
    list_of_action = ['+', '-', '*']
    random_action = randint(0, 2)
    action = list_of_action[random_action]
    summ = first_number_of_example + second_number_of_example
    delta = first_number_of_example - second_number_of_example
    multi = first_number_of_example * second_number_of_example
    list_of_calculation = [summ, delta, multi]
    match action:
        case '+':
            answ = str(list_of_calculation[random_action])
            question = (f'{first_number_of_example} {action}'
                        f' {second_number_of_example}')
            return question, answ
        case '-':
            answ = str(list_of_calculation[random_action])
            question = (f'{first_number_of_example} {action}'
                        f' {second_number_of_example}')
            return question, answ
        case '*':
            answ = str(list_of_calculation[random_action])
            question = (f'{first_number_of_example} {action}'
                        f' {second_number_of_example}')
            return question, answ
