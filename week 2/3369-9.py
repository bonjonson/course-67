lst = input()
x = input()
ind = 0
spisok = lst.split()
if x in spisok:
    if spisok.count(x) > 1:
        indexes = [i for i, a in enumerate(spisok) if a == x]
        print(*indexes[::])
    else:
        lst = spisok.index(x)
        print(lst)        
else:
    print('Отсутствует')
