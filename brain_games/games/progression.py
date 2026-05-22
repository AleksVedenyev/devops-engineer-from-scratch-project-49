import random


def random_number():
    return random.randint(1, 50)


def game_condition():
    return 'What number is missing in the progression?'


def make_progression():
    progression = []
    start = random_number()
    step = random_number()
    length = random.randint(5, 10)
    for index in range(length):
        current_element = start + index * step
        progression.append(current_element)
    return progression


def question_and_correct_answer():
    progression = make_progression()
    random_index = random.randint(0, len(progression) - 1)
    answer = str(progression[random_index])
    progression[random_index] = '..'
    question = (f'Question: {" ".join(str(x) for x in progression)}')
    return question, answer


