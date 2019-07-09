a = input().split()
b = list()
last = int(len(a)-1) #последний индекс
summa = int() #сумма соседей
for i in range(len(a)):
  a[i] = int(a[i])
  if i == 0 and len(a) > 1:
    summa = (int(a[1])) + (int(a[last]))
    b.append(summa)
  elif i == 0 and len(a) == 1:
    summa = a[0]
    b.append(summa)
  elif 0 < i < last:
    summa = (int(a[i-1])) + (int(a[i+1]))
    b.append(summa)
  elif i == last:
    summa = (int(a[last-1])) + (int(a[0]))
    b.append(summa)
print(*b)
