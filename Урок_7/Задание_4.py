n = int(input())
for i in range(1, n+1):

    if i >= 2 and i <= 8 and i >= 128 and i <= 256 and i >= 1024 and i <= 2048:
        continue
    print(i)
