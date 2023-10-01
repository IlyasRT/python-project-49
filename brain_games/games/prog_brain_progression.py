from random import randint

print('brain-progression')
DESCR = 'What number is missing in the progression?'


def initial_data():


    def check_progression():
        length_of_progression = randint(5, 10)
        position_of_unknown_element = randint(0, length_of_progression - 1)
        delta_of_progression = randint(1, 5)
        x = (length_of_progression * delta_of_progression) + 1
        progression = []
        for i in range(delta_of_progression, x, delta_of_progression):
            progression.append(i)
        ue = progression[position_of_unknown_element]
        progression[position_of_unknown_element] = '..'
        return progression, ue
    progression, ue = check_progression()
    expression = progression
    answ = str(ue)
    return expression, answ
