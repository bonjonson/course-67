num = int(input()) #принимаем число
a = num * 2
line = list(range(1, num+1)) #записываем его в виде списка поэлементно
outline = ""
outline2 = list() #запасной список
l = len(line)
for i in line: #для всех значений i в line 
    outline = (str(line[i - 1]) + " ") * line[i - 1]
    outline2.append(outline)
outline3 = ''.join(outline2)
if 100 > num >=47 and num % 3 == 2:
  a = a + 2
elif 100 < num < 1000 and num % 3 == 2:
  a = a + 1
elif 44 < num < 100 and num % 2 == 0:
  a = a + 2
outline4 = outline3[:a]
outline5 = outline4.split()
print(*outline5[::])
