n = int(input())
cnt = int()
for i in range(n):
    cnt = 0
    num = int(input())
    if num % 2 == 0:
        cnt += 1
        print(cnt)
if cnt == 0:
    print('yes')
else:
    print('no')
