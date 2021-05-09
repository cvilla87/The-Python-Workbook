# Write a program that begins by reading an amount of euros and cents.
# Then your program should compute and display the denominations of the coins
# that should be used to give that amount of change to the user.
# The change should be given using as few coins as possible.
from math import floor


def exchange(amount_cents, coin):
    number_coins = floor((amount_cents / coin))
    amount_cents -= number_coins * coin
    print(f"Give {number_coins} coins of {coin}.")
    print(f"Pending exchange: {amount_cents}")
    return amount_cents


ONE_CENT = 1
FIVE_CENT = 5
QUARTER_EUR = 25
FIFTY_CENT = 50
ONE_EUR = 100

price = '9.87'  # In euros. String format simulating it was an input.

price_in_cents = (int(price.split('.')[0]) * 100) + int(price.split('.')[1])
print(price_in_cents)

while price_in_cents != 0:
    if price_in_cents > ONE_EUR:
        price_in_cents = exchange(price_in_cents, ONE_EUR)
    elif price_in_cents > FIFTY_CENT:
        price_in_cents = exchange(price_in_cents, FIFTY_CENT)
    elif price_in_cents > QUARTER_EUR:
        price_in_cents = exchange(price_in_cents, QUARTER_EUR)
    elif price_in_cents > FIVE_CENT:
        price_in_cents = exchange(price_in_cents, FIVE_CENT)
    else:  # price_in_cents > ONE_CENT:
        price_in_cents = exchange(price_in_cents, ONE_CENT)
