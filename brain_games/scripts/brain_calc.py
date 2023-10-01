#!/usr/bin/env python3

from brain_games.scripts.start import start_game
from brain_games.games import prog_brain_calc


def main():
    start_game(prog_brain_calc)


if __name__ == '__main__':
    main()
