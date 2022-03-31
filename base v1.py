
import random

def yes_no(question_text):
    while True:

        answer = input(question_text)



        if answer == "Y" or instruction == "Yes":
            answer = "Yes"
            return answer

        elif answer == "N" or instruction == "No":
            answer = "No"
            return answer

        else:
            print("Please answer (Y or N) ")


def instruction():
    print()
    print(formatter("-" "How to play"))
    print()
    print("choose a starting amount to play with - must be between $1-$10 ")
    print()
    print("Then press <enter> to play, You will get a random token which might"
          "be a horse, a zebra, a donkey, or a unicorn.")
    print()
    print("It cost $1 to play each round but, depending on your prize, you"
          "could win some of your money back. These are the payout amounts:\n"
          "\tUnicorn: $5 (balance increases by $4)\n"
          "\tHorse: $0.50 (balance decreases by $0.50)\n"
          "\tZebra: $0.50 (balance decreases by $0.50)\n"
          "\tDonkey: $0.00 (balance decreases by $1)\n")
    print("\nSee if you can avoid donkeys, get the unicorns, and finish with "
          "more money than you started with.\n")
    print("-" * 50)
    print()
    print("How to play")
    print()
    print("Rules")
    print()


def num_check(question, low, high):
    error = "That was not valid input\n" \
            "please enter a number between {} and {}\n".format(low, high)


    while True:
        try:
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


def generate_token(the_balance):

    rounds_played = 0
    play_again = ""

    while play_again != "x":
        rounds_played += 1
        number = random.randint(1, 100)

        if 1 <= number <= 5:
            token = "unicorn"
            the_balance += 4
            print(formatter("-", "Congratulations, you got a unicorn"))
            print()

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
    return the_balance


def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


print(formatter("-", "Welcome to Lucky Unicorn"))
print()

played_before = yes_no("have you played this game before? ")

if played_before == "No":
    instruction()



starting_balance = num_check("How much would you like to play with $", 1, 10)
print(f"You are playing with ${starting_balance}")

closing_balance = generate_token(starting_balance)
print("thanks for playing")
print(f"you started with ${starting_balance:.2f}")
print(f"and leave with ${closing_balance:.2f}")
print()
print(formatter("-", "Goodbye"))
