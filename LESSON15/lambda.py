# def squared(num): return num * num


# print(squared(2))

"""

def squared(num): return num * num


print(squared(2))

# addTwo = lambda num : num + 2

# print(addTwo(7))


def addTwo(num): return num + 2


print(addTwo(7))


def sum_total(a, b): return a + b
# lambda a, b : a + b


print(sum_total(2, 7))


'''-------------------------------------------'''


def funcBuilder(x):
    return lambda num: num + x


addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(11))


# lambda num : num * num

import numbers
numbers = [2, 7, 11, 12, 17, 24, 27]

squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))


'''----------------------------'''


odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))

"""

from functools import reduce

# lambda acc, curr: acc + curr

numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)

print(sum(numbers, 10))

lambda acc, curr: acc + len(curr)
