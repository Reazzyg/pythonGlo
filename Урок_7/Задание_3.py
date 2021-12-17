a = int(input())
length = len(str(a))
cnt = 0
for i in range(length):
    letter = a % 10
    if letter != 1:
        a = a // 10
    elif letter == 1:
        cnt += 1
if cnt != 0:
    print('yes')
else:
    print('no')
