from math import sqrt


def even(a):
    return a % 2 == 0


def square(a):
    return [4 * a, a * a, a * sqrt(2)]


def first_last(a):
    return [a[0], a[-1]]


def repeat(a):
    s = set()
    for x in a:
        if x in s:
            return True
        s.add(x)
    return False


lst = input().split()


print(first_last(lst))
print(repeat(lst))
