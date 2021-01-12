from itertools import accumulate, zip_longest


x = [1, 2, 3, 4, 5]

for y in accumulate(x):
    print(y)


a = [1, 2]
b = ["a", "b", "c"]

for y in zip(a, b):
    print(y)

for y in zip_longest(a, b):
    print(y)
