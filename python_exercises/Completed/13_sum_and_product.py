def calculateSum(numbers):
    if len(numbers) == 0:
        #print(0)
        return 0
    
    calc_sum = 0
    for num in numbers:
        calc_sum += num
    #print(calc_sum)
    return calc_sum

def calculateProduct(numbers):
    if len(numbers) == 0:
        #print(1)
        return 1
    
    product = 1
    for num in numbers:
        product *= num
    #print(product)
    return product

# calculateSum([])
# calculateSum([2, 4, 6, 8, 10])
# calculateProduct([])
# calculateProduct([2, 4, 6, 8, 10])

assert calculateSum([]) == 0
assert calculateSum([2, 4, 6, 8, 10]) == 30
assert calculateProduct([]) == 1
assert calculateProduct([2, 4, 6, 8, 10]) == 3840