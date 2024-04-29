def ordinalSuffix(number):
    ordinal = str(number)
    if ordinal[-2:] == "11" or ordinal[-2:] == "12" or ordinal[-2:] == "13":
        print(f"{ordinal}th")
        return ordinal + "th"
    elif ordinal[-1] == "1":
        print(f"{ordinal}st")
        return ordinal + "st"
    elif ordinal[-1] == "2":
        print(f"{ordinal}nd")
        return ordinal + "nd"
    elif ordinal[-1] == "3":
        print(f"{ordinal}rd")
        return ordinal + "rd"
    else:
        print(f"{ordinal}th")
        return ordinal + "th"

assert ordinalSuffix(0) == '0th'
assert ordinalSuffix(1) == '1st'
assert ordinalSuffix(2) == '2nd'
assert ordinalSuffix(3) == '3rd'
assert ordinalSuffix(4) == '4th'
assert ordinalSuffix(10) == '10th'
assert ordinalSuffix(11) == '11th'
assert ordinalSuffix(12) == '12th'
assert ordinalSuffix(13) == '13th'
assert ordinalSuffix(14) == '14th'
assert ordinalSuffix(101) == '101st'

# ordinalSuffix(0)
# ordinalSuffix(1)
# ordinalSuffix(2)
# ordinalSuffix(3)
# ordinalSuffix(4)
# ordinalSuffix(10)
# ordinalSuffix(11)
# ordinalSuffix(12)
# ordinalSuffix(13)
# ordinalSuffix(14)
# ordinalSuffix(101)