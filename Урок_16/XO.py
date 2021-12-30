def create_field():
    field = []
    for i in range(3):
        field.append(['*'] * 3)
    return field


def print_field(field):
    for i in range(3):
        for j in range(3):
            print(field[i], [j], end='')
        print()


def win():


def end_game(field):
    if win(field):
        return True

    for i in range(3):


field = create_field()
print_field(field)

current_symbol = 'X'

while not win(field):
    print_field(field)
    print('Введите номер строки и номер столбца')
    row = int(input())
    column = int(input())
    field[row-1][column - 1] = current_symbol

    if current_symbol == 'X':
        current_symbol = 'O'
    else:
        current_symbol = 'X'
if current_symbol == 'X':
    print('won  O')
else:
    print('won X')
