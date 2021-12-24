def calc_star_day(date):
    table = date.split('.')
    for i in range(len(table)):
        a = int(table.pop(i))
        table.insert(i, a)
    if table[0]*table[1] == table[2] % 100:
        print('True')
    else:
        print('false')


print('Введите дату')
date = input()
calc_star_day(date)
