n = int(input())
cnt = int()
for i in range(n):
    cnt = 0
    num = int(input())
    if num % 2 == 0:
        cnt += 1
if cnt != 0:
    print('no')
else:
    print('yes')
