from math import *
import operator
a = float(input())
b = float(input())
oper = str(input())
ops = {'+':operator.add, '-':operator.sub, '/':operator.truediv, '*':operator.mul, 'mod':operator.mod, 'pow':operator.pow, 'div':operator.floordiv}
if oper in ops:
    if (oper in ['/','div','mod']) and b == 0:
        print('Деление на 0!')
    else:
        result = ops[oper](a, b)
        print(result)
else:
    print('Wrong operation')