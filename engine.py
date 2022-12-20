from itertools import repeat
from random import randint

import prompt

SIZE = 7
BULLET = 1
MAGAZINE = list(repeat(1, SIZE - BULLET))
MAGAZINE.extend(repeat(0, BULLET))


def prepare_gun(bullet_index=0, magazine=MAGAZINE, scroll_magazine=False):
    """
    Make virtual gun.

    Args:
        bullet_index: current index of trigger,
        magazine: current position of magazine,
        scroll_magazine: need to scroll magazine.

    Returns:
        dict of gun condition.
    """
    if scroll_magazine:
        wheel_mag = randint(0, SIZE - 1)
        magazine = MAGAZINE[wheel_mag:] + MAGAZINE[:wheel_mag]
    return {
        'magazine': magazine,
        'shot': magazine[bullet_index],
    }


def run_game():
    """Start common game module."""
    attempt = prepare_gun(scroll_magazine=True)
    bullet_index = 0
    while attempt['shot']:
        print('Lucky this time!')
        question = prompt.string('Try again? (y/n) ')
        if question == 'y':
            question = prompt.string('Wheel magazine? (y/n) ')
            if question == 'y':
                attempt = prepare_gun(
                    magazine=attempt['magazine'], scroll_magazine=True,
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


if __name__ == '__main__':
    run_game()
