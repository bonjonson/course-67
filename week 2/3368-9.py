a = input().split()
b = int()
for i in range(len(a)):
  a[i] = int(a[i])
  b = b + a[i]
print(b)