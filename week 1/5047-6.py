n = int(input())
if (0 <= n <= 1000):
    if (n == 1 or n % 100 != 11 and n % 10 == 1):
        print(n, 'программист')
    elif (n in [2, 3, 4] or n % 100 not in [12, 13, 14] and n % 10 in [2, 3, 4]):
        print(n, 'программиста')
    else:
        print(n, 'программистов')
else:
    print('Wrong volume')