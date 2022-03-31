

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

        else:
            token = "horse"
            the_balance -= .5


    print(f"round {rounds_played}. Token: {token}, Balance: ${the_balance:.2f}")
    if the_balance < 1:
        print("\nSorry you ran out of money ")
        play_again = "x"
    else:
        play_again = input("\nDo you want to play another round?\n<enter? to play "
                           "again or 'x' to exit ").lower()
    print()

print("thanks for playing")
print(f"you started with ${test_amount:.2f}")
print(f"and leave with ${the_balance:.2f}")
print("goodbye")

