n = int(input())
total = int()
for i in range(1, n+1):
    if i % 10 == 1 or i % 10 == 3 or i % 10 == 7:
        total += i
print(total)
