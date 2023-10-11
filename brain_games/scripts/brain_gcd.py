#!/usr/bin/env python3

from brain_games.game_engine import run_game_process
from brain_games.games import prog_brain_gcd


def main():
    run_game_process(prog_brain_gcd)


if __name__ == '__main__':
    main()
