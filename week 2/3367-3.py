gen = input()
l = len(gen)
gq = gen.lower().count('g')
qg = gen.lower().count('c')
proc = (gq + qg) / l * 100
print(proc)