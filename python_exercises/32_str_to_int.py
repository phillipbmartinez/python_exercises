def convertStrToInt(stringNum):
    integerNum = 0

    DIGITS_STR_TO_INT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    if stringNum[0] == "-":
        isNegative = True
        stringNum = stringNum[1:] 
    else:
        isNegative = False

    for digit in stringNum:
        integerNum = (integerNum * 10) + DIGITS_STR_TO_INT[digit]

    if isNegative == True:
        print(-integerNum)
        return -integerNum
    else:
        print(integerNum)
        return integerNum

# convertStrToInt("-25")
# convertStrToInt("41096")

for i in range(-10000, 10000):
    assert convertStrToInt(str(i)) == i
print("All tests passed.")