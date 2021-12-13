num = int(input())
last = num % 1000
last1 = last // 100
last2 = last // 10 % 10
last3 = last % 10

print('У числа', num, 'сумма последних трех цифр равна', last1+last2+last3)
