

import random

test_amount = 5
the_balance = test_amount

rounds_played = 0
play_again = ""

while play_again != "x":
    rounds_played += 1
    number = random.randint(6,36)

    if 1 <= number <= 5:
        token = "unicorn"
        the_balance += 4

    elif 6 <= number <= 36:
        token = "donkey"
        the_balance -= 1

    else:
        if number % 2 == 0:
            token = "zebra"
            the_balance -= 0.5
