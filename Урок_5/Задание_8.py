n = int(input())
minimum = int()
maximum = int()
for i in range(n):
    number = int(input())

    if number > maximum:
        maximum = number
    elif number < minimum:
        minimum = number
print('max', maximum)
print('min', minimum)
