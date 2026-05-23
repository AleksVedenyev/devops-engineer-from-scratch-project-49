import random


def random_number():
    return random.randint(1, 50)


def random_operator():
    operators = ['+', '-', '*']
    return random.choice(operators)


GAME_CONDITION = 'What is the result of the expression?'


def question_and_correct_answer():
    first_random_num = random_number()
    second_random_num = random_number()
    operator = random_operator()
    question = (
        f'Question: {first_random_num} {operator} {second_random_num}'
    )
    match operator:
        case '+':
            answer = str(first_random_num + second_random_num)
        case '-':
            answer = str(first_random_num - second_random_num)
        case '*':
            answer = str(first_random_num * second_random_num)
    return question, answer


