import random


def random_number():
    return random.randint(1, 100)


def is_even(number):
    return number % 2 == 0


def game_condition():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def question_and_correct_answer():
    random_num = random_number()
    question = (
        f'Question: {random_num}'
    )
    answer = 'yes' if is_even(random_num) else 'no'
    return question, answer