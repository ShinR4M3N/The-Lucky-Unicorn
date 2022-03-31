balance = int(input("How much do you want to play with (between 1-10) $"))

while not 1 <= balance <=10:
    print("try again")
    balance = int(input("How much do you want to play with (between 1-10) $"))
print(f"are using {balance} dollars")
