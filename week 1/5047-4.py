from math import sqrt
figure = input()
if figure == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    s = float(sqrt(p * (p - a) * (p - b) * (p - c)))
elif figure == 'прямоугольник':
    a = int(input())
    b = int(input())
    s = float(a * b)
elif figure == 'круг':
    r = int(input())
    s = float(3.14 * pow(r, 2))
print(s)