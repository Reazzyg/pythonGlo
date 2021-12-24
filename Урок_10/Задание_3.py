def month(number):
    if number == 1 or number == 3 or number == 5 or number == 7 or number == 8 or number == 10 or number == 11:
        print('31')
    elif number == 4 or number == 6 or number == 9 or number == 11:
        print('30')
    elif number == 2:
        print('28')
    elif number > 12 or number < 1:
        print('введите корректное значение')


number = int(input())
month(number)
