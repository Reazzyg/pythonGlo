total = 100


def calc_delivery(ammount):
    all = 0
    for i in range(ammount):
        all = 1+(ammount*0.5)
    print(total*all)


print('Введите количество товаров:')
ammount = int(input())
calc_delivery(ammount)
