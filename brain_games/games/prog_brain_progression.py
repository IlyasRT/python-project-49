from random import randint
DESCR = 'What number is missing in the progression?'
LOWER_BOUND_OF_PROGRESSION = 6
UPPER_BOUND_OF_PROGRESSION = 10
LOWER_BOUND_UNKNOWN_ELEMENT = 0
LOWER_BOUND_DIFFERENCE = 1
UPPER_BOUND_DIFFERENCE = 5


def get_example_and_answer():
    initial_term, last_elem, difference, index = calc_prog()
    progres = build_prog(initial_term, last_elem, difference, index)
    question, unknown_element = build_question(progres, index)
    answ = str(unknown_element)
    return question, answ


def calc_prog():
    len_prog = randint(LOWER_BOUND_OF_PROGRESSION, UPPER_BOUND_OF_PROGRESSION)
    index_unknown_element = randint(LOWER_BOUND_UNKNOWN_ELEMENT, len_prog - 1)
    difference = randint(LOWER_BOUND_DIFFERENCE, UPPER_BOUND_DIFFERENCE)
    initial_term = difference
    last_elem = initial_term + (len_prog - 1) * difference
    return initial_term, last_elem, difference, index_unknown_element


def build_prog(initial_term, last_elem, difference, index_unknown_element):
    progression = []
    for i in range(initial_term, last_elem + 1, difference):
        progression.append(i)
    return progression


def build_question(progres, index_unknown_element):
    unknown_element = progres[index_unknown_element]
    progres[index_unknown_element] = '..'
    prog_str = list(map(lambda x: str(x), progres))
    prog_for_print = " ".join(prog_str)
    return prog_for_print, unknown_element
