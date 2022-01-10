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

right_answers_ammount = 0


def count_right_answers(user_answer, right_answer, right_answers_ammount):
    if user_answer == right_answer:
        right_answers_ammount += 1
    return right_answers_ammount


def randomize_questions(questions):
    random_index = randint(0, len(questions))
    question = questions.pop([random_index])
    return question


while True:
    user_name = input('Введите Ваше имя:')
    for i in range(len(questions)):
        print(i+1, randomize_questions(questions))
        user_answer = int(input())
        right_answer = answers[i]
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
