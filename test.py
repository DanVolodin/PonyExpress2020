from math import sqrt
from math import hypot


class Rectangle:
    def __init__(self, list_of_dots):
        dot1 = list_of_dots[0]
        dot2 = list_of_dots[1]
        dot3 = list_of_dots[2]
        dot4 = list_of_dots[3]
        minx = min(dot1[0], dot2[0], dot3[0], dot4[0])
        maxx = max(dot1[0], dot2[0], dot3[0], dot4[0])
        miny = min(dot1[1], dot2[1], dot3[1], dot4[1])
        maxy = max(dot1[1], dot2[1], dot3[1], dot4[1])
        self.dot_1 = [minx, miny]
        self.dot_2 = [minx, maxy]
        self.dot_3 = [maxx, maxy]
        self.dot_2 = [maxx, miny]
        self.a = maxx - minx
        self.b = maxy - miny

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


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


lst = list()

for i in range(4):
    dot = [int(a) for a in input().split()]
    lst.append(dot)

rec = Rectangle(lst)
print(rec.perimeter(), rec.area())