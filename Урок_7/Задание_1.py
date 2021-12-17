num = int(input())
while num:
    num = int(input())
    if num < 10:
        continue
    if num > 100:
        break
    print(num)
