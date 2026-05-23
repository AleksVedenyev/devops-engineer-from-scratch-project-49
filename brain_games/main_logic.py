import prompt

from brain_games.cli import greet, welcome_user

COUNT_ROUNDS = 3


def main_logic(game):
    greet()
    name = welcome_user()
    print(game.GAME_CONDITION)
    for _ in range(COUNT_ROUNDS):
        question, correct_answer = game.question_and_correct_answer()
        print(question)
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(
                (f"'{user_answer}' is wrong answer ;(. Correct answer was "
                 f"'{correct_answer}'.\nLet's try again, {name}!")
            )
            return
    print(f'Congratulations, {name}!')