#!/usr/bin/env python3

from brain_games.games.start import start_game
from brain_games.games import prog_brain_calc 
from brain_games.games.prog_brain_calc import initial_data #пришлось импортировать отдельно

def main():
    start_game(prog_brain_calc)

if __name__ == '__main__':
    main()
