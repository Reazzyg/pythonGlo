a = int(input())
cnt = 0
while a != 0:
    last_digit = a % 10
    a = a // 10
    if last_digit == 5:
        cnt += 1
print(cnt)

