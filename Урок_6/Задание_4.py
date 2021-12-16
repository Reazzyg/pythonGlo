n = int(input())
minimum = int()
maximum = int()
if n >= 10:
    minimum = n
    maximum = 0
    while n != 0:
        last_digit = n % 10
        n = n // 10
        if last_digit > maximum:
            maximum = last_digit
        elif last_digit < minimum:
            minimum = last_digit
    print('min:', minimum)
    print('max:', maximum)
else:
    print('Введите число большее или равное 10')
