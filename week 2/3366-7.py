a = int(input())
b = int(input())
s = 0
ar = 0
l = [i for i in range(a, b + 1) if not i%3]
ar = sum(l)/len(l)
print(float(ar))