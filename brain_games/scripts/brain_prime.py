#!/usr/bin/env python3

from brain_games.game_engine import create_game_process
from brain_games.games import prog_brain_prime


def main():
    create_game_process(prog_brain_prime)


if __name__ == '__main__':
    main()
