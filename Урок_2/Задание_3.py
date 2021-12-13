a = int(input())

first = a//100
second = a % 100//10
third = a % 10
print('Сумма цифр числа', a, 'равно', first+second+third)
print('Произведение цифр числа', a, 'равно', first*second*third)
