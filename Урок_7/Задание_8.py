
n = int(input())
cnt = 0
for i in range(n,1, -1):
  while i != 0:
    last_digit = i % 10
    i = i // 10
    if last_digit == 5:
        cnt += 1
print(cnt)
