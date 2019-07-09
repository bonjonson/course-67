a = int(input())
b = int(input())
c = int(input())
my_list = [a, b, c]
s = a + b + c
ma = max(my_list)
mi = min(my_list)
other = s - ma - mi
print(ma)
print(mi)
print(other)