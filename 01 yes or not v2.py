instruction = input("have you played this game before? (Y/N) ")

if instruction == "Y" or instruction == "Yes":
    print("Program Continues")

elif instruction == "N" or instruction == "No":
    print("Display instruction")

else:
    print("Please answer (Y or N) ")

print(f"You have entered: {instruction}")
