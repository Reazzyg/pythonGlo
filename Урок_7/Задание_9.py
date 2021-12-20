n = int(input())
total = n
while total > 9:
    n = total
    total = 0
    while n != 0:
        last_digit = n % 10
        n = n // 10
        total += last_digit
print(total)
