
r = int(input())
k = int(input())
n = int(input())
kop = k/100
price = r+kop
sum = price*n
sum_kop = sum*100 % 100
print('За', n, 'мячей', 'надо заплатить', int(
    sum), 'рублей и', int(sum_kop), 'копеек')
