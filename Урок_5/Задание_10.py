
n = int(input())
cnt = 0
for i in range(n):

    num = int(input())
    if num % 2 == 0:
        cnt += 1
if cnt == 0:
    print('yes')
else:
    print('no')
