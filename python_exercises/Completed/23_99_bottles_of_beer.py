for numberOfBottles in range(99, 0, -1):
    if numberOfBottles == 2:
        print(f"{numberOfBottles} bottles of beer on the wall,")
        print(f"{numberOfBottles} bottles of beer,")
        print("Take one down,")
        print("Pass it around,")
        print(f"{numberOfBottles - 1} bottle of beer on the wall,\n")
    elif numberOfBottles == 1:
        print(f"{numberOfBottles} bottle of beer on the wall,")
        print(f"{numberOfBottles} bottle of beer,")
        print("Take one down,")
        print("Pass it around,")
        print("No more bottles of beer on the wall!")
    else:
        print(f"{numberOfBottles} bottles of beer on the wall,")
        print(f"{numberOfBottles} bottles of beer,")
        print("Take one down,")
        print("Pass it around,")
        print(f"{numberOfBottles - 1} bottles of beer on the wall,\n")
