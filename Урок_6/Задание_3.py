a = int(input())
num = a
total = 0
while a != 0:
    last_digit = a % 10
    total += last_digit
    a = a // 10
if num % total == 0:
    print('yes')
else:
    print('no')
