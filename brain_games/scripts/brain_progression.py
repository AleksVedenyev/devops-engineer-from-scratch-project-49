from brain_games.games.progression import (
    game_condition,
    question_and_correct_answer,
)
from brain_games.main_logic import main_logic


def main():
    main_logic(question_and_correct_answer, game_condition)


if __name__ == "__main__":
    main()