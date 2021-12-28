from random import randint


def valid_answer(answer):
    while True:
        if answer == '+' or answer == '-':
            break
        else:
            print('Введите, пожалуйста + или -')
            answer = input()
            continue
    return answer


def ask_question(question):
    print(question, 'Введите + или -')
    answer = input()
    answer = valid_answer(answer)
    if answer == '+':
        return True
    else:
        return False


def valid_digit(input_info):
    while True:
        if input_info.isdigit():
            input_info = int(input_info)
            break
        else:
            print('Введите число или цифру')
            input_info = input()
            continue
    return input_info


def generate_password(length, chars):
    password = ''
    for i in range(length):
        random_index = randint(0, len(chars)-1)
        password += chars[random_index]
    return password


while True:

    print('Привет, Я генератор паролей, я задам немколько вопросв и сгенерирую пароль. \nНачнем')
    print('Сколько паролей вы хотите сгенерировать?')
    ammount = input()
    ammount = valid_digit(ammount)
    print('Введите длину пароля')
    length = input()
    length = valid_digit(length)

    digits_enabled = ask_question('Включать ли цифры?')
    latin_lowercase_enabled = ask_question(
        'Включать ли строчные латинские буквы?')
    latin_uppercase_enabled = ask_question(
        'Включать ли заглавные латинские буквы')
    russian_lowercase_enabled = ask_question(
        'Включать ли строчные русские буквы?')
    russian_uppercase_enabled = ask_question(
        'Включать ли заглавные русские буквы?')
    punctuation_enabled = ask_question('Включать ли специальные символы?')
    enabled_chars = ''
    digits = '0123456789'
    latin_lowercase_letters = 'qwertyuiopasdfghjklzxcvbnm'
    latin_uppercase_letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    russian_lowercase_letters = 'йцукенгшщзфывапролдячсмить'
    russian_uppercase_letters = 'ЙЦУКЕНГШЩЗФЫВАПРОЛДЯЧСМИТЬ'
    punctuation = '!@#$%^&*()_-+=:;",.'

    if digits_enabled:
        enabled_chars += digits
    if latin_lowercase_enabled:
        enabled_chars += latin_lowercase_letters
    if latin_uppercase_enabled:
        enabled_chars += latin_uppercase_letters
    if russian_lowercase_enabled:
        enabled_chars += russian_lowercase_letters
    if russian_uppercase_enabled:
        enabled_chars += russian_uppercase_letters
    if punctuation_enabled:
        enabled_chars += punctuation
    password = generate_password(length, enabled_chars)
    print(password)
