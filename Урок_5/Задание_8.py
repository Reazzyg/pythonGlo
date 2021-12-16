
n = int(input())
minimum = int(input())
maximum = int(input())
for i in range(n-2):
    number = int(input())
    if number > maximum:
        maximum = number
    elif number < minimum:
        minimum = number
print('max', maximum)
print('min', minimum)
