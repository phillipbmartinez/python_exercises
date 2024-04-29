def median(numbers):
    if len(numbers) == 0:
        print("This was an empty list: []")
        return None
    
    numbers.sort()
    
    if len(numbers) % 2 != 0:
        m = len(numbers) // 2
        print(f"The median of the list: {numbers}, is {numbers[m]}")
        return numbers[m]
    if len(numbers) % 2 == 0:
        m1 = len(numbers) // 2
        m2 = (len(numbers) // 2) + 1
        a = (m1 + m2) / 2
        print(f"The median of the list: {numbers}, is {a}")
        return a

# median([])
# median([1, 2, 3])
# median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8])
# median([3, 7, 10, 4, 1, 9, 6, 2, 8])

assert median([]) == None
assert median([1, 2, 3]) == 2
assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5
assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6
assert median([10, 11, 13, 15, 16, 23, 26]) == 15

# import random
# random.seed(42)
# testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]
# for i in range(1000):
#     random.shuffle(testData)
#     assert median(testData) == 6