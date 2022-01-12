from random import randint
from pathlib import Path


def get_questions():

    questions = [
        'вопрос 1',
        'вопрос 2',
        'вопрос 3',
        'вопрос 4',
        'вопрос 5',
        'вопрос 6',
        'вопрос 7',
        'вопрос 8',
        'вопрос 9',
        'вопрос 10',
        'вопрос 11',
        'вопрос 12'
    ]
    return questions


def get_answers():
    answers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    return answers


def valid_answer_end(answer):
    while True:
        if answer == '+' or answer == '-':
            break
        else:
            print('Введите, пожалуйста + или -')
            answer = input()
            continue
    return answer


def valid_answer_digit(answer):
    while True:
        if answer.isdigit():
            answer = int(answer)
            break
        else:
            print('Ответ должен состоять из цифр')
            answer = input()
            continue
    return answer


def randomize_question_index(questions):
    random_index = randint(0, len(questions)-1)
    return random_index


def randomize_questions(questions, random_index):
    question = questions.pop(random_index)
    return question


def calc_results(questions_amount, right_answers_ammount):
    right_answers_percent = 100/questions_amount*right_answers_ammount
    if right_answers_percent == 0:
        return results[0]
    elif right_answers_percent > 0 and right_answers_percent <= 20:
        return results[1]
    elif right_answers_percent > 20 and right_answers_percent <= 40:
        return results[2]
    elif right_answers_percent > 40 and right_answers_percent <= 60:
        return results[3]
    elif right_answers_percent > 60 and right_answers_percent <= 80:
        return results[4]
    elif right_answers_percent > 80 and right_answers_percent <= 100:
        return results[5]


file = open('Урок_18/info.txt', 'a')
while True:
    # path = Path('info.txt')

    questions = get_questions()
    answers = get_answers()
    right_answers_ammount = 0
    qeutions_ammount = len(questions)

    results = [
        'идиот \n',
        'кретин \n',
        'дурак \n',
        'нормальный \n',
        'талант \n',
        'гений \n',
    ]

    user_name = input('Введите Ваше имя:')
    for i in range(len(questions)):
        random_index = randomize_question_index(questions)
        question = randomize_questions(questions, random_index)
        print(i+1, question)
        user_answer = input()
        user_answer = valid_answer_digit(user_answer)
        right_answer = answers[random_index]
        if user_answer == right_answer:
            right_answers_ammount += 1
        answers.pop(random_index)
    result = calc_results(qeutions_ammount, right_answers_ammount)
    resume = [user_name, right_answers_ammount, result, ]
    resume = " ".join(map(str, resume))
    print(resume)
    file.write(resume)
    print('Правильных ответов:', right_answers_ammount)
    print(user_name, ',Вы -', result)
    print('Если хотите сыграть еще раз введите +, если не хотите введите -')
    answer = input()
    answer = valid_answer_end(answer)
    if answer == '+':
        right_answers_ammount = 0
        continue
    else:
        print('Спасибо за участие')
        file.close()
        break
print(f'имя', 'Кол-во правильных ответов', 'Результат')
file = open('Урок_18/info.txt', 'r')
print(file.read())
