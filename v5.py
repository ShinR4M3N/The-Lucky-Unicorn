def yes_no(question_text):
    while True:

        answer = input(question_text)

        instruction = input("have you played this game before? (Y/N) ")

        if answer == "Y" or instruction == "Yes":
            answer = "Yes"
            return answer

        elif answer == "N" or instruction == "No":
            answer = "No"
            return answer

        else:
            print("Please answer (Y or N) ")


instruction = yes_no("have you played this game before? ")
print(f"You have entered: {instruction}")
print()
having_fun = yes_no("Are you having fun? ")
print(f"You have entered: {having_fun}")
