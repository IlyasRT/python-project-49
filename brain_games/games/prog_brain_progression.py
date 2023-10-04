from random import randint
print('brain-progression')
DESCR = 'What number is missing in the progression?'


def initial_data():
    first, last, delta, index = calc_prog()
    progres, unk_el = build_prog(first, last, delta, index)
    expression = build_question(progres)
    answ = str(unk_el)
    return expression, answ


def calc_prog():
    len_prog = randint(5, 10)
    index_unk_el = randint(0, len_prog - 1)
    delta_prog = randint(1, 5)
    first_prog_el = delta_prog
    last_prog_el = (len_prog * delta_prog) + 1
    return first_prog_el, last_prog_el, delta_prog, index_unk_el


def build_prog(first_prog_el, last_prog_el, delta_prog, index_unk):
    prog = []
    for i in range(first_prog_el, last_prog_el, delta_prog):
        prog.append(i)
    ue = prog[index_unk]
    prog[index_unk] = '..'
    return prog, ue


def build_question(progres):
    prog_str = list(map(lambda x: str(x), progres))
    prog_for_print = " ".join(prog_str)
    return prog_for_print
