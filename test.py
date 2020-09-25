from math import sqrt


def even(a):
    return a % 2 == 0


def square(a):
    return [4 * a, a * a, a * sqrt(2)]


def first_last(a):
    return [a[0], a[-1]]


lst = input().split()

print(first_last(lst))
