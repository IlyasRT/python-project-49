from random import randint
import prompt 
from brain_games.cli import welcome_user
print(f'brain-prog')
def brain_prog():
    name = welcome_user()
    correction_of_user_answer = True
    count = 0
    while count < 3:
        length_of_progression = randint(5, 10)
        #print('length_of_progression=',length_of_progression)
        position_of_unknown_element = randint(0, length_of_progression-1)
        #print(position_of_unknown_element)
        delta_of_progression = randint(1, 10)
        x=length_of_progression*delta_of_progression+1
        progression=[]
        for i in range(delta_of_progression,x,delta_of_progression):
            #print(i, end=' ')
            progression.append(i)
        unknown_element=progression[position_of_unknown_element]
        #print(unknown_element)
        progression[position_of_unknown_element]='..'
        

        print(f'What number is missing in the progression?')
        correction_of_user_answer = True
        print(*progression)
        user_answer = prompt.string('Your answer: ')
        if int(user_answer) == unknown_element:
            count += 1
            print(f'Correct!')
        else:
            count = 3
            correction_of_user_answer = False
            print(f'\'{user_answer}\' is wrong answer;(.Correct answer was \'{unknown_element}\'. Let\'s try again, {name}!')
    if correction_of_user_answer == True:
        print(f'Congratulations, {name}!')
