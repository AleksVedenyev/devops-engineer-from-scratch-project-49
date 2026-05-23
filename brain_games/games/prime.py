import math
import random


def random_number():
    return random.randint(2, 100)


def is_prime(number):
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for num in range(3, int(math.sqrt(number) + 1), 2):
        if number % num == 0:
            return False
    return True
        

GAME_CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def question_and_correct_answer():
    random_num = random_number()
    question = (
        f'Question: {random_num}'
    )
    answer = 'yes' if is_prime(random_num) else 'no'
    return question, answer