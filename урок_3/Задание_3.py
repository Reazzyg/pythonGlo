num = int(input())
n1 = num // 100000
n2 = num // 10000 % 10
n3 = num // 1000 % 10
n4 = num // 100 % 10
n5 = num % 100 // 10
n6 = num % 10
first_half = n1 + n2 + n3
second_half = n4 + n5 + n6

if first_half == second_half:
    print('Билет',  num, 'счастливый')
else:
    print('Билет', num, 'НЕ счастливый')
