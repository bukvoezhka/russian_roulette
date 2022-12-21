from itertools import repeat
from random import randint

import prompt

SIZE = 7
BULLET = 1
MAGAZINE = list(repeat(1, SIZE - BULLET))
MAGAZINE.extend(repeat(0, BULLET))
YES = ('yes', 'y')
NO = ('no', 'n')
START = 'start'
NEXT = 'next'
SPIN = 'spin'


def prepare_gun(bullet_index=0, magazine=MAGAZINE, spin_cylinder=False):
    """
    Make virtual gun.

    Args:
        bullet_index: current index of trigger,
        magazine: current position of magazine,
        spin_cylinder: need to spin magazine.

    Returns:
        dict of gun condition.
    """
    if spin_cylinder:
        wheel_mag = randint(0, SIZE - 1)
        magazine = MAGAZINE[wheel_mag:] + MAGAZINE[:wheel_mag]
    return {
        'magazine': magazine,
        'shot': magazine[bullet_index],
    }


def validate_answer(answer):
    """
    Validate user input.

    Args:
        answer: current user input.

    Returns:
        correct answer.
    """
    if answer.lower() in YES or answer.lower() in NO:
        return answer.lower()
    print('Wrong input.')


def ask_question(question, step):
    """
    Generate question for player in game session.

    Args:
        question: question depending on game status,
        step: current game step.

    Returns:
        user answer.
    """
    ask_player = prompt.string(question)
    if validate_answer(ask_player) is None:
        play_round(step)
    return ask_player


def play_round(step):
    """
    Handle current game round.

    Args:
        step: current game step.

    Returns:
        user action.
    """
    if step == START:
        return ask_question('Want to try your luck? (y|n): ', START)
    if step == NEXT:
        return ask_question('Try again? (y|n): ', NEXT)
    if step == SPIN:
        return ask_question('Spin the cylinder? (y|n): ', SPIN)


def run_game():
    """Start common game module."""
    step = play_round(START)
    if step in YES:
        attempt = prepare_gun(spin_cylinder=True)
        bullet_index = 0
        while attempt['shot']:
            print('Lucky this time!')
            step = play_round(NEXT)
            if step in YES:
                step = play_round(SPIN)
                if step in YES:
                    bullet_index = 0
                    attempt = prepare_gun(
                        magazine=attempt['magazine'], spin_cylinder=True,
                    )
                else:
                    bullet_index += 1
                    attempt = prepare_gun(
                        magazine=attempt['magazine'], bullet_index=bullet_index,
                    )
            else:
                print('See you next time.')
                break
        if not attempt['shot']:
            print('Oops! Not lucky this time..')
    elif step in NO:
        print('Come back any time!')


if __name__ == '__main__':
    run_game()
