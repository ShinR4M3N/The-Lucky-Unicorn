import random

tokens = ["unicorn",
          "horse","horse","horse",
          "donkey", "donkey", "donkey",
          "zebra","zebra","zebra"]
starting_balance = 100
balance = starting_balance


for item in range(500):
    token = random.choice(tokens)


    if token == "unicorn":
        balance += 4
    elif token == "donkey":
        balance -= 1
    else:
        balance -= .50


print(f"Starting Balance = ${starting_balance:.2f}")
print(f"Final Balance = ${balance:.2f}")
