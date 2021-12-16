num = int(input())
cnt = 0
total = 0
while num != 0:
    cnt += 1
    total += num
    num = int(input())
print(total/cnt)
