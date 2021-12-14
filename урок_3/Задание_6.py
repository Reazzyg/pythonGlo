num = int(input())
if num == 0:
    print('Green')
elif num >= 1 and num <= 10 and num % 2 == 0:
    print('black')
elif num >= 1 and num <= 10 and num % 2 != 0:
    print('red')
elif num >= 19 and num <= 28 and num % 2 == 0:
    print('black')
elif num >= 19 and num <= 28 and num % 2 != 0:
    print('red')
elif num >= 11 and num <= 18 and num % 2 == 0:
    print('black')
elif num >= 11 and num <= 18 and num % 2 != 0:
    print('red')
elif num >= 29 and num <= 36 and num % 2 == 0:
    print('black')
elif num >= 29 and num <= 36 and num % 2 != 0:
    print('red')
elif num < 0 or num > 36:
    print('Error')
