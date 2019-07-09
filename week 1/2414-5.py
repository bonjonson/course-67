A = int(input())
B = int(input())
if A > B:
    print('Неверное значение B')
    B = int(input())
H = int(input())
if A <= H <= B:
        print('Это нормально')
elif A > H:
        print('Недосып')
elif H > B:
        print('Пересып')
