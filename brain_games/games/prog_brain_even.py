from random import randint
print('brain-even')
DESCR = 'Answer "yes" if the number is even, otherwise answer "no".'


def initial_data():
    expression = randint(1, 10)
    
    
    def check_even(x):
        if int(x % 2) == 0:
            answer = True
        elif int(x % 2) != 0:
            answer = False
        return answer
    if check_even(expression) == True:
        answ = 'yes'
    else:
        answ = 'no'
    return expression, answ
    

