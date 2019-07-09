abcdef = str(input())
qwerty = list(str(abcdef))
half1 = int(qwerty[0]) + int(qwerty[1]) + int(qwerty[2])
half2 = int(qwerty[3]) + int(qwerty[4]) + int(qwerty[5])
if half1 == half2:
    print('Счастливый')
else:
    print('Обычный')