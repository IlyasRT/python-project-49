#!/usr/bin/env python3

from brain_games.games.start import start_game
from brain_games.games import prog_brain_even
from brain_games.games.prog_brain_even import initial_data

def main():
    start_game(prog_brain_even)

if __name__ == '__main__':
    main()
