
from math import floor


r = int(input())
k = int(input())
n = int(input())
kop = k/100
price = r+kop
sum = price*n
sum_kop = round(sum*100) % 100
print('За', n, 'мячей', 'надо заплатить', floor(
    sum), 'рублей и', sum_kop, 'копеек')
