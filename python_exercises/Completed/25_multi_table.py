print('  | 1  2  3  4  5  6  7  8  9 10')
print('--+------------------------------')
for row in range(1, 11):
    print(str(row).rjust(2) + "|", end="")
    for column in range(1, 11):
        print(str(row * column).rjust(2) + " ", end="")
    print()