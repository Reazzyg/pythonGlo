import random


def valid_secret(right_border):
    if right_border.isdigit():
        right_border = int(right_border)
    else:
        return False


def secret(right_border):
    secret_number = random.randint(1, right_border)
    return secret_number


print('Добро пожаловать в игру "Загадай число"')
print('Загадайте число')


while True:
    while True:
        print('Введите правую границу диапазона:')
        right_border = input()
        if not valid_secret(right_border):
            right_border = int(right_border)
            secret_number = secret(right_border)
            break
        else:
            continue
    store = []
    num = 1
    for i in range(num, right_border+1):
        store.append(num)
        num += 1
    print(store)
    mid = len(store) // 2
    low = 0
    high = len(store) - 1
    cnt = 1
    while True:
        print('Если ваше число больше, чем', mid,
              'введите ">", если ваше число меньше чем', mid, 'введите "<"', 'если ваше число рано', mid, 'введите "="')
        value = input()
        if value == '>':
            low = mid + 1
            cnt += 1
            mid = (low + high) // 2
        elif value == '<':
            high = mid - 1
            cnt += 1
            mid = (low + high) // 2
        elif value == '=':
            print('Ура, победа, ваше число =', mid)
            print('Угадано за', cnt, 'попыток')
            break
    print('Если хотите сыграть еще раз введите "+", если не хотите введите "-"')
    decision = input()
    if decision == '+':
        continue
    else:
        break
