#Ends in 1 = -st, ends in 2 = -nd, ends in 3 = -rd, ends in 4 - 9 = -th
def ordinalSuffix(number):
    numberStr = str(number)
    print(numberStr[-1])

    if numberStr[-2:] in ("11", "12", "13"):
        print(f"{number}th")
    elif numberStr[-1] == "1":
        print(f"{number}st")
    elif numberStr[-1] == "2":
        print(f"{number}nd")
    elif numberStr[-1] == "3":
        print(f"{number}rd")
    else:
        print(f"{number}th")


ordinalSuffix(0)
ordinalSuffix(1)
ordinalSuffix(2)
ordinalSuffix(3)
ordinalSuffix(4)
ordinalSuffix(10)
ordinalSuffix(11)
ordinalSuffix(12)
ordinalSuffix(13)
ordinalSuffix(14)
ordinalSuffix(101)
ordinalSuffix(102)
ordinalSuffix(103)

"""assert ordinalSuffix(0) == '0th'
assert ordinalSuffix(1) == '1st'
assert ordinalSuffix(2) == '2nd'
assert ordinalSuffix(3) == '3rd'
assert ordinalSuffix(4) == '4th'
assert ordinalSuffix(10) == '10th'
assert ordinalSuffix(11) == '11th'
assert ordinalSuffix(12) == '12th'
assert ordinalSuffix(13) == '13th'
assert ordinalSuffix(14) == '14th'
assert ordinalSuffix(101) == '101st'"""