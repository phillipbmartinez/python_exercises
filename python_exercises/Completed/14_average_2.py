def average(numbers):
    if len(numbers) == 0:
        return None

    sum_total = 0
    for number in numbers:
        sum_total += number
    avg = sum_total / len(numbers)
    return avg


assert average([1, 2, 3]) == 2
assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
assert average([12, 20, 37]) == 23
assert average([0, 0, 0, 0, 0]) == 0
import random
random.seed(42)
testData = [1, 2, 3, 1, 2, 3, 1, 2, 3]
for i in range(1000):
    random.shuffle(testData)
    assert average(testData) == 2
print()
print("All tests passed.")