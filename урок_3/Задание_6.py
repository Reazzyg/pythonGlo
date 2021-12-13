num = int(input())
if num == 0:
    print('Green')
elif num >= 1 and num <= 10 or num >= 19 and num <= 28:
    print('black')
elif num >= 11 and num <= 18 or num >= 29 and num <= 36:
    print('red')
elif num < 0 or num > 36:
    print('Error')
