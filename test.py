from math import sqrt


def even(a):
    return a % 2 == 0


def square(a):
    return [4 * a, a * a, a * sqrt(2)]


x = int(input())
print(even(x), square(x))
