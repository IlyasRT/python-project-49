#!/usr/bin/env python3
from brain_games.cli_brain_even import main
from random import randint
from prompt import string
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import main

def main():
	name='Ilyas'
	print(f'Answer "yes" if the number is even, otherwise answer "no".')
	count = 0
	correction_of_user_answer = True
	while count < 3:
	    random_number = randint(1, 10)
	    print(f'Question: {random_number}')
	    user_answer = prompt.string('Your answer:').lower()
	    if (random_number % 2 == 0 and user_answer == 'yes'.lower()) or (random_number % 2 != 0 and user_answer == 'no'.lower()):
		count += 1
		print(f'Correct!')

	    else:
		count = 3
		correction_of_user_answer = False
		print(f'\'yes\' is wrong answer ;\(. Correct answer was \'no\'. Let\'s try again, {name}!')
	if correction_of_user_answer==True:
	    print(f'Congratulations, {name}! {count} - {correction_of_user_answer}')

    
    

main()
