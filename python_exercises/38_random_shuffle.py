import random

def shuffle(values):
    for v in range(len(values)):
        random_index = random.randint(0, len(values) - 1)
        values[v], values[random_index] = values[random_index], values[v]

random.seed(42)
# Perform this test ten times:
for i in range(10):
    testData1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    shuffle(testData1)
    # Make sure the number of values hasn't changed:
    assert len(testData1) == 10
    # Make sure the order has changed:
    assert testData1 != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Make sure that when re-sorted, all the original values are there:
    assert sorted(testData1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Make sure an empty list shuffled remains empty:
testData2 = []
shuffle(testData2)
assert testData2 == []
print("All tests passed.")