from random import randint
import random


def valid_answer(answer):
    while True:
        if answer == '+' or answer == '-':
            break
        else:
            print('Введите, пожалуйста + или -')
            answer = input()
            continue
    return answer


right_answers_ammount = 0


def count_right_answers(user_answer, right_answer, right_answers_ammount):
    if user_answer == right_answer:
        right_answers_ammount += 1
    return right_answers_ammount


def randomize_question_index(questions):
    random_index = randint(0, len(questions)-1)
    return random_index


def randomize_questions(questions, random_index):
    question = questions.pop(random_index)
    return question


while True:
    questions = [
        'вопрос 1',
        'вопрос 2',
        'вопрос 3',
        'вопрос 4',
        'вопрос 5'
    ]

    answers = [1, 2, 3, 4, 5]

    results = [
        'идиот',
        'кретин',
        'дурак',
        'нормальный',
        'талант',
        'гений',
    ]

    user_name = input('Введите Ваше имя:')
    for i in range(len(questions)):
        random_index = randomize_question_index(questions)
        question = randomize_questions(questions, random_index)
        print(i+1, question)
        user_answer = int(input())
        right_answer = answers.pop(random_index)
        right_answers_ammount = count_right_answers(
            user_answer, right_answer, right_answers_ammount)
    print('Правильных ответов:', right_answers_ammount)
    print(user_name, ',Вы -', results[right_answers_ammount])
    print('Если хотите сыграть еще раз введите +, если не хотите введите -')
    answer = input()
    answer = valid_answer(answer)
    if answer == '+':
        right_answers_ammount = 0
        continue
    else:
        print('Спасибо за участие')
        break
