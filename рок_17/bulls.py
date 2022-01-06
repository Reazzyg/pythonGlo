from random import randint


def generate_secret_word():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    secret_word = ''
    for i in range(4):
        random_index = randint(0, len(digits)-1)
        secret_word += str(digits[random_index])
        digits.pop(random_index)
    return secret_word


def calc_bulls_count(user_word, secret_word):
    cnt = 0
    for i in range(len(secret_word)):
        if secret_word[i] == user_word[i]:
            cnt += 1
    return cnt


def calc_cows_count(user_word, secret_word):
    cnt = 0
    for i in range(len(user_word)):
        if secret_word[i] != user_word[i] and user_word[i] in secret_word:
            cnt += 1
    return cnt


def valid_answer(answer):
    while True:
        if answer == '+' or answer == '-':
            break
        else:
            print('Введите, пожалуйста + или -')
            answer = input()
            continue
    return answer


def valid_input(user_input):
    while True:
        if len(user_input) == len(secret_word):
            for i in range(len(user_input)):
                if ord(user_input[i]) >= 48 and ord(user_input[i]) <= 57:
                    for j in range(len(user_input)):
                        if not user_input.count(user_input[j]) > 1:
                            break
                        else:
                            print('все цифры должны быть разными')
                            user_input = input()
                            continue
                else:
                    print('Введите цифры от 0 до 9')
                    user_input = input()
                    continue
        else:
            print('ввдите число, состоящее из', len(secret_word),  'символов')
            user_input = input()
            continue
        return user_input


secret_word = generate_secret_word()

while True:
    while True:
        print('')
        print('Введите число из', len(secret_word), 'цифр')
        user_word = input()
        user_word = valid_input(user_word)
        bulls_count = calc_bulls_count(user_word, secret_word)
        cows_count = calc_cows_count(user_word, secret_word)
        print(bulls_count, 'быков', cows_count, 'коров')
        if not bulls_count == 4:
            continue
        elif bulls_count == 4:
            print('victory')
            print(' Если хотите сыграть еще раз введите +, если не хотите введите -')
            answer = input()
            answer = valid_answer(answer)
            if answer == '+':
                continue
            elif answer == '-':
                break
    break
