
error = "please enter a whole number between 1 - 10\n"
valid = False

while not valid:
    try:

        balance = int(input("How much do you want to play with (between 1-10) $"))

        if 0 < balance <=10:
            print(f"are using {balance} dollars")
            valid = True
        else:
            print(error)

    except ValueError:
        print(error)

