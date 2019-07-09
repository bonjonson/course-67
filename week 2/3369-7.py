summa = 0
square = 0
while True:
    a = int(input())
    summa += a
    square += a*a
    if summa == 0:
        break
print(square)   