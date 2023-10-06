from random import randint
print('brain-progression')
DESCR = 'What number is missing in the progression?'


def get_example_and_answer():
    initial_term, last, difference, index = calc_prog()
    progres = build_prog(initial_term, last, difference, index)
    expression, unknown_element = build_question(progres, index)
    answ = str(unknown_element)
    return expression, answ


def calc_prog():
    len_prog = randint(5, 10)
    index_unknown_element = randint(0, len_prog - 1)
    difference_2 = randint(1, 5)
    initial_term_2 = difference_2
    last_elem = (len_prog * difference_2) + 1
    return initial_term_2, last_elem, difference_2, index_unknown_element


def build_prog(initial_term_2, last_elem, difference_2, index_unknown_element):
    progression = []
    for i in range(initial_term_2, last_elem, difference_2):
        progression.append(i)
    return progression


def build_question(progres, index_unknown_element):
    unknown_element = progres[index_unknown_element]
    progres[index_unknown_element] = '..'
    prog_str = list(map(lambda x: str(x), progres))
    prog_for_print = " ".join(prog_str)
    return prog_for_print, unknown_element
