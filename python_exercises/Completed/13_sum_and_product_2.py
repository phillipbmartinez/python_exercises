def calculateSum(numbers):
    if len(numbers) == 0:
        return 0

    sum_total = 0
    for number in numbers:
        sum_total += number
    return sum_total


def calculateProduct(numbers):
    if len(numbers) == 0:
        return 1
    
    product_total = 1
    for number in numbers:
        product_total *= number
    return product_total

# calculateSum([])
# calculateSum([2, 4, 6, 8, 10])
# calculateProduct([])
# calculateProduct([2, 4, 6, 8, 10])

assert calculateSum([]) == 0
assert calculateSum([2, 4, 6, 8, 10]) == 30
assert calculateProduct([]) == 1
assert calculateProduct([2, 4, 6, 8, 10]) == 3840
print()
print("All tests passed.")