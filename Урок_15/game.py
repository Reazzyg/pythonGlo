from random import randint


def update_user_word(secret_word, user_word, char):
    new_user_word = ''
    for i in range(len(secret_word)):
        if secret_word[i] == char:
            new_user_word += char
        else:
            new_user_word += user_word[i]
    return new_user_word


def valid_answer(answer):
    while True:
        if answer == '+' or answer == '-':
            break
        else:
            print('Введите, пожалуйста + или -')
            answer = input()
            continue
    return answer


def valid_letter(letter):
    while True:
        if letter.isdigit() or ord(letter) < 1072 or ord(letter) > 1103:
            print('введите букву русского алфавита')
            letter = input().lower()
            continue
        else:
            letter = letter
            break
    return letter


def letter_was_used(letter, letter_storage):
    while True:
        for i in range(len(letter_storage)-1):
            if letter == letter_storage[i]:
                print('вы уже вводили эту букву')
                letter = input().lower()
                letter = valid_letter(letter)
                letter_storage.append(letter)
                continue
        break
    return letter


def print_stars(secret_word):
    word = ''
    for i in range(len(secret_word)):
        word += '*'
    return word


while True:
    question_storage = ['вопрос 1', 'вопрос 2', 'вопрос 3',
                        'вопрос 4', 'вопрос 5', 'вопрос 6',
                        'вопрос 7', 'вопрос 8', 'вопрос 9',
                        'вопрос 10']
    answer_storage = ['первое', 'второе', 'третье', 'четвертое',
                      'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое', 'десятое']
    question_number = randint(0, len(question_storage))
    question = question_storage[question_number]
    secret_word = answer_storage[question_number]
    print(question)
    user_word = print_stars(secret_word)
    print(user_word)
    letter_storage = []
    cnt = 0
    while user_word != secret_word:
        print('Введите букву')
        user_char = input().lower()
        user_char = valid_letter(user_char)
        letter_storage.append(user_char)
        user_char = letter_was_used(user_char, letter_storage)
        print(letter_storage)
        if len(user_char) != 1:
            continue
        new_user_word = update_user_word(
            secret_word, user_word, user_char)
        if user_word == new_user_word:
            print('такой буквы нет')
            cnt += 1
        else:
            print('такая буква есть')
            cnt += 1
        user_word = new_user_word
        print(user_word)
    print('Поздравляем, вы выиграли! Количество попыток:', cnt,
          ' Если хотите сыграть еще раз введите +, если не хотите введите -')
    answer = input()
    answer = valid_answer(answer)
    if answer == '+':
        continue
    else:
        break
