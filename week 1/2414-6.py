year = int(input())
if year < 1900 or year > 3000:
    print('Enter valid volume')
    year = int(input())
if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print('Високосный')
else:
    print('Обычный')