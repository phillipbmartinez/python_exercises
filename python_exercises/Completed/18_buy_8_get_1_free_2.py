def getCostOfCoffee(numberOfCoffees, pricePerCoffee):
    totalPrice = 0
    cupsTillFreeCoffee = 8

    while numberOfCoffees > 0:
        numberOfCoffees -= 1

        if cupsTillFreeCoffee == 0:
            cupsTillFreeCoffee = 8
        else:
            totalPrice += pricePerCoffee
            cupsTillFreeCoffee -= 1
    return totalPrice


# getCostOfCoffee(7, 2.50)
# getCostOfCoffee(8, 2.50)
# getCostOfCoffee(9, 2.50)
# getCostOfCoffee(10, 2.50)

assert getCostOfCoffee(7, 2.50) == 17.50
assert getCostOfCoffee(8, 2.50) == 20
assert getCostOfCoffee(9, 2.50) == 20
assert getCostOfCoffee(10, 2.50) == 22.50

for i in range(1, 4):
    assert getCostOfCoffee(0, i) == 0
    assert getCostOfCoffee(8, i) == 8 * i
    assert getCostOfCoffee(9, i) == 8 * i
    assert getCostOfCoffee(18, i) == 16 * i
    assert getCostOfCoffee(19, i) == 17 * i
    assert getCostOfCoffee(30, i) == 27 * i
print("All tests passed.")