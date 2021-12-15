n = int(input())
total = 1

for i in range(1, n+1):
    if i % 10 == 2 or i % 10 == 9:
        total *= i
if total > 1:
    print(total)
else:
    print(0)
