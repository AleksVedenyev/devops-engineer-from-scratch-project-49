import random


def random_number():
    return random.randint(1, 100)


def game_condition():
    return 'Find the greatest common divisor of given numbers.'


def question_and_correct_answer():
    first_random_num = random_number()
    second_random_num = random_number()
    question = (f'Question: {first_random_num} {second_random_num}')
    a = first_random_num
    b = second_random_num
    temp = b
    if b == 0:
        answer = str(a)
        return question, answer
    while b != 0:
        b = a % b
        a = temp
        temp = b
    answer = str(a)
    return question, answer


