gen = input().split() #вводим строку
gen.sort()
gen2 = "" #результирующая пустая строка
i=1
#print(gen)
#print(len(gen))
while i <= len(gen): #пока i не выходит за длину строки
    count = 1 #счетчик по умолчанию
    while (i<=len(gen)-1) and (gen[i] == gen[i-1]):
#пока i <= длины gen-1 и индекс gen == индекс-1 gen      
        count = count + 1 #увеличиваем cnt
        i+=1 #увеличиваем индекс
    if count > 1:
      gen2 = gen2 + gen[i-1] + " "
    #конкатинируем строку
    i+=1 #увеличиваем индекс
print(gen2) #выводим результат
