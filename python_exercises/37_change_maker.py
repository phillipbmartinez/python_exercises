def makeChange(amount):
    if amount == 0:
        return None

    change = {}
    amount_left = amount
    if amount_left < 25:
        pass
    else:
        change["quarters"] = amount_left // 25
        amount_left = amount_left % 25
    
    if amount_left < 10:
        pass
    else:
        change["dimes"] = amount_left // 10
        amount_left = amount_left % 10

    if amount_left < 5:
        pass
    else:
        change["nickels"] = amount_left // 5
        amount_left = amount_left % 5
    
    if amount_left < 1:
        pass
    else:
        change["pennies"] = amount_left // 1
        amount_left = amount_left % 1
    
    # print(change)
    return change


assert makeChange(30) == {'quarters': 1, 'nickels': 1}
assert makeChange(10) == {'dimes': 1}
assert makeChange(57) == {'quarters': 2, 'nickels': 1, 'pennies': 2}
assert makeChange(100) == {'quarters': 4}
assert makeChange(125) == {'quarters': 5}
print("All tests passed.")