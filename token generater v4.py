import random

tokens = ["unicorn",
          "horse","horse","horse",
          "donkey", "donkey", "donkey",
          "zebra","zebra","zebra"]
starting_balance = 100
balance = starting_balance


for item in range(10):
    number = random.randint(1,100)


    if 1 <= number <=5:
        token = "unicorn"
        balance += 4
    elif 6 <= number <= 36:
        token = "donkey"
        balance -= 1
    else:
        if number % 2 == 0:
            token = "zebra"
            balance -= 0.5
        else:
            token = "horse"
            balance -= .5

    print(f"Token: {token}, Balance: ${balance:.2f}")

print()
print(f"Starting Balance = ${starting_balance:.2f}")
print(f"Final Balance = ${balance:.2f}")
