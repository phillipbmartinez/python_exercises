def median(numbers):
    if len(numbers) == 0:
        # print("None")
        return None
    
    if len(numbers) % 2 == 0:
        numbers.sort()
        n1 = numbers[len(numbers) // 2]
        n2 = numbers[len(numbers) // 2] - 1
        # print(n1)
        # print(n2)
        # print((n1 + n2)/2)
        return (n1 + n2)/2


    if len(numbers) % 2 != 0:
        numbers.sort()
        # print(numbers[len(numbers) // 2])
        return numbers[len(numbers) // 2]

# median([])
# median([1, 2, 3])
# median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8])
# median([3, 7, 10, 4, 1, 9, 6, 2, 8])

assert median([]) == None
assert median([1, 2, 3]) == 2
assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5
assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6
import random
random.seed(42)
testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]
for i in range(1000):
    random.shuffle(testData)
    assert median(testData) == 6
print("All tests passed.")