# TODO

from cs50 import get_float
from cs50 import get_int

while True:
    dollars = get_float("Change owed:")
    if dollars >= 0:
        break

cents = round(dollars *100)
coins = 0

# for quarters
while cents >= 25:
    cents -= 25
    coins += 1

# for dimes
while cents >= 10:
    cents -= 10
    coins += 1

# for nickels
while cents >= 5:
    cents -= 5
    coins += 1

# for pennies
while cents >= 1:
    cents -= 1
    coins += 1

print(coins)