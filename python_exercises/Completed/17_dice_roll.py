import random

def rollDice(numberOfDice):
    dice_roll_total = 0
    for d in range(numberOfDice):
        roll = random.randint(1, 6)
        dice_roll_total += roll
    return dice_roll_total

# roll_1 = print(rollDice(1000))
# roll_2 = print(rollDice(10))
# roll_3 = print(rollDice(3))
# roll_4 = print(rollDice(2))
# roll_5 = print(rollDice(1))

assert rollDice(0) == 0
assert rollDice(1000) != rollDice(1000)
for i in range(1000):
    assert 1 <= rollDice(1) <= 6
    assert 2 <= rollDice(2) <= 12
    assert 3 <= rollDice(3) <= 18
    assert 100 <= rollDice(100) <= 600