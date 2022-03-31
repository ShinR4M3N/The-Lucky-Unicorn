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
    print("How to play")
    print()
    print("Rules")
    print()
    print("program continues")
    print()


played_before = yes_no("have you played this game before? ")

if played_before == "No":
    instruction()
else:
    print("Program continues")

