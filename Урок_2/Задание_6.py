from math import *
ammount = int(input())
a1 = ammount // 1000
a2 = ammount // 100 % 10
a3 = ammount % 100 // 10
a4 = ammount % 10
print(max(a1, a2, a3, a4))
