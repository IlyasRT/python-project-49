from random import randint
DESCR = 'What number is missing in the progression?'


def get_example_and_answer():
    initial_term, last_elem, difference, index = calc_prog()
    progres = build_prog(initial_term, last_elem, difference, index)
    question, unknown_element = build_question(progres, index)
    answ = str(unknown_element)
    return question, answ


def calc_prog():
    len_prog = randint(5, 10)
    index_unknown_element = randint(0, len_prog - 1)
    difference = randint(1, 5)
    initial_term = difference
    last_elem = initial_term + (len_prog - 1) * difference
    return initial_term, last_elem, difference, index_unknown_element


def build_prog(initial_term, last_elem, difference, index_unknown_element):
    progression = []
    for i in range(initial_term, last_elem, difference):
        progression.append(i)
    return progression


def build_question(progres, index_unknown_element):
    unknown_element = progres[index_unknown_element]
    progres[index_unknown_element] = '..'
    prog_str = list(map(lambda x: str(x), progres))
    prog_for_print = " ".join(prog_str)
    return prog_for_print, unknown_element
