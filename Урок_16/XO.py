def create_field():
    field = []
    for i in range(3):
        field.append(['*'] * 3)

    return field


def print_field(field):
    for i in range(3):
        for j in range(3):
            print(field[i][j], end='')
        print()


def win(field):
    for i in range(3):
        if field[i][0] != '*' and field[i][0] == field[i][1] == field[i][2]:
            return True
    for i in range(3):
        if field[0][i] != '*' and field[0][i] == field[1][i] == field[2][i]:
            return True
    for i in range(3):
        if field[0][0] != '*' and field[0][0] == field[1][1] == field[2][2]:
            return True
    for i in range(3):
        if field[0][2] != '*' and field[0][2] == field[1][1] == field[2][0]:
            return True

    return False


def is_draw(field):
    cnt = 0
    for i in range(3):
        for j in range(3):
            if field[i][j] == '*':
                cnt += 1
    if cnt == 0:
        return True
    else:
        return False


def end_game(field):

    if win(field):
        return True

    elif not win(field):
        for i in range(3):
            for j in range(3):
                if field[i][j] == '*':
                    return False


def check_if_was_used(field):
    if field[row - 1][column - 1] != '*':
        return False
    else:
        return True


def valid_answer(answer):
    while True:
        if answer == '+' or answer == '-':
            break
        else:
            print('Введите, пожалуйста + или -')
            answer = input()
            continue
    return answer


def valid_input(number):
    while True:
        if number.isdigit():
            number = int(number)
            if number >= 1 and number <= 3:
                number = int(number)
                break
            else:
                print('введите число от 1 до 3')
                number = input()
        else:
            print('Введите число или цифру')
            number = input()
            continue
    return number


# def check_if_was_used(row_store, col_store):
#     row_store = []
#     col_store = []
#     for i in range(len(row_store)):
#         if row_store.count(row):
#             print('Эта клетка уже занята')
#     for j in range(len(col_store)):
#         if col_store.count(col)


while True:
    field = create_field()
    current_symbol = 'X'
    while not end_game(field):
        print_field(field)
        print('Введите номер строки и номер столбца')
        row = input()
        row = valid_input(row)
        column = input()
        column = valid_input(column)
        while True:
            if check_if_was_used(field):
                field[row - 1][column - 1] = current_symbol
                break
            else:
                print('эта клетка уже занята')
                row = input()
                row = valid_input(row)
                column = input()
                column = valid_input(column)
                continue
        if current_symbol == 'X':
            current_symbol = 'O'
        else:
            current_symbol = 'X'
    print_field(field)
    if is_draw(field):
        print('draw')
    elif current_symbol == 'X':
        print('won  O')
    else:
        print('won X')
    print(' Если хотите сыграть еще раз введите +, если не хотите введите -')
    answer = input()
    answer = valid_answer(answer)
    if answer == '+':
        continue
    else:
        break
