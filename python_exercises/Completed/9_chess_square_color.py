def getChessSquareColor(column, row):
    if (column >= 8) or (column < 0) or (row >= 8) or (row < 0):
        print("")
        return ""
    elif (column % 2 == 0) and (row % 2 == 0):
        print("white")
        return "white"
    elif (column % 2 != 0) and (row % 2 != 0):
        print("white")
        return "white"
    elif (column % 2 == 0) and (row % 2 != 0):
        print("black")
        return "black"
    elif (column % 2 != 0) and (row % 2 == 0):
        print("black")
        return "black"

getChessSquareColor(-1, 0)
getChessSquareColor(0, 0)
getChessSquareColor(1, 0)
getChessSquareColor(0, 1)
getChessSquareColor(7, 7)
getChessSquareColor(0, 8)
getChessSquareColor(2, 9)

"""
assert getChessSquareColor(0, 0) == 'white'
assert getChessSquareColor(1, 0) == 'black'
assert getChessSquareColor(0, 1) == 'black'
assert getChessSquareColor(7, 7) == 'white'
assert getChessSquareColor(0, 8) == ''
assert getChessSquareColor(2, 9) == ''
"""

"""
def getChessSquareColor(column, row):
    # If the column and row is out of bounds, return a blank string:
    if column < 1 or column > 8 or row < 1 or row > 8:
        return ''

    # If the even/oddness of the column and row match, return 'white':
    if column % 2 == row % 2:
        return 'white'
    # If they don't match, then return 'black':
    else:
        return 'black'

assert getChessSquareColor(1, 1) == 'white'
assert getChessSquareColor(2, 1) == 'black'
assert getChessSquareColor(1, 2) == 'black'
assert getChessSquareColor(8, 8) == 'white'
assert getChessSquareColor(0, 8) == ''
assert getChessSquareColor(2, 9) == ''
"""