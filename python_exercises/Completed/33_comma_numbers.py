def commaFormat(number):
    # Convert the number to a string:
    number = str(number)
    # Remember the fractional part and remove it from the number, if any:
    if '.' in number:
        fractionalPart = number[number.index('.'):]
        number = number[:number.index('.')]
    else:
        fractionalPart = ''
    # Create a variable to hold triplets of digits and the
    # comma-formatted string as it is built:
    triplet = ""
    commaNumber = ""

    # Loop over the digits starting on the right side and going left:
    for i in range(len(number) - 1, -1, -1):
        # Add the digits to the triplet variable:
        triplet = number[i] + triplet
        # When the triplet variable has three digits, add it with a
        # comma to the comma-formatted string:
        if len(triplet) == 3:
            commaNumber = triplet + ',' + commaNumber
            # Reset the triplet variable back to a blank string:
            triplet = ""

    # If the triplet has any digits left over, add it with a comma
    # to the comma-formatted string:
    if triplet != '':
        commaNumber = triplet + ',' + commaNumber

    # Return the comma-formatted string:
    print(commaNumber[:-1] + fractionalPart)
    return commaNumber[:-1] + fractionalPart


# commaFormat(1000000)
# commaFormat(12315)

assert commaFormat(1) == '1'
assert commaFormat(10) == '10'
assert commaFormat(100) == '100'
assert commaFormat(1000) == '1,000'
assert commaFormat(10000) == '10,000'
assert commaFormat(100000) == '100,000'
assert commaFormat(1000000) == '1,000,000'
assert commaFormat(1234567890) == '1,234,567,890'
assert commaFormat(1000.123456) == '1,000.123456'
print("All tests passed.")