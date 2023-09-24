#!/usr/bin/env python3

from brain_games.games.start import start_game
from brain_games.games import prog_brain_calc 
from brain_games.games.prog_brain_calc import brain_calc #пришлось импортировать отдельно

#from brain_games.games.prog_brain_calc import * 
#from brain_games.games import prog_brain_calc * 
#from brain_games.games.prog_brain_calc import brain_calc


def main():
    start_game(prog_brain_calc)
    brain_calc()  # без него программа только выводит 'What is the result of the expression?' и останавливается, потом понял, что это из за return, но без него не вытащить name из функции

if __name__ == '__main__':
    main()
