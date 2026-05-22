import prompt

from brain_games.cli import greet, welcome_user


def main_logic(question_and_correct_answer, game_condition):
    greet()
    name = welcome_user()
    print(game_condition())
    for _ in range(3):
        question, correct_answer = question_and_correct_answer()
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