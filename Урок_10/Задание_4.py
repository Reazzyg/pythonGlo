total = 100


def calc_delivery(ammount):
    all = 0
    if ammount > 0:
        for i in range(ammount-1):
            all = (ammount-1)*50
        print(total+all)
    elif ammount == 0:
        print('0')


print('Введите количество товаров:')
ammount = int(input())
calc_delivery(ammount)
