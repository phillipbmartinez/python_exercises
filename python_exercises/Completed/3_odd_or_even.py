def isOdd(number):
    if number % 2 != 0:
        print(f"{number} is odd.")
    else:
        print(f"{number} is even.")

def isEven(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
    
isOdd(42)
isOdd(9999)
isOdd(-10)
isOdd(-11)
isOdd(3.1415)
isEven(42)
isEven(9999)
isEven(-10)
isEven(-11)
isEven(3.1415)