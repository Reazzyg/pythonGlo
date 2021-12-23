adress = input()
cnt = 0
storage = adress.split('.')
for i in range(4):
    if int(storage[i]) < 255 and int(storage[i]) >= 0:
        cnt += 1
    else:
        cnt -= 1
if cnt == 4:
    print('yes')
else:
    print('no')
