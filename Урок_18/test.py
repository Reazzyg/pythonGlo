from random import randint
from pathlib import Path


class QuestionStorage():
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def get_questions():

        questions = [
            QuestionStorage('вопрос 1', 1),
            QuestionStorage('вопрос 2', 2),
            QuestionStorage('вопрос 3', 3),
            QuestionStorage('вопрос 4', 4),
            QuestionStorage('вопрос 5', 5),
            QuestionStorage('вопрос 6', 6),
            QuestionStorage('вопрос 7', 7),
            QuestionStorage('вопрос 8', 8),
            QuestionStorage('вопрос 9', 9),
            QuestionStorage('вопрос 10', 10),
            QuestionStorage('вопрос 11', 11),
            QuestionStorage('вопрос 12', 12),

        ]
        return questions


class User():
    def __init__(self, name, right_answers_ammount, result):
        self.name = name
        self.right_answers_ammount = right_answers_ammount
        self.result = result

    def add_user_info(name, right_answers_ammount, result):
        user_info_file = open('user_info.txt', 'a')
        user_info = [
            User(name, right_answers_ammount, result)
        ]
        user_info_file.write(
            f'{user_info[0].name:10}{user_info[0].result:15}{user_info[0].right_answers_ammount:25}\n')
        return user_info

    def show_previous_results():
        name = 'имя'
        right_answers_ammount = 'Кол-во правильных ответов'
        result = 'Результат'
        user_info_file = open('user_info.txt', 'r')
        print(f'{name:10}{result:15}{right_answers_ammount:30}')
        return user_info_file.read()


class UserResultStorage():
    def __init__(self, name, result):
        self.name = name
        self.result = result

    def add_results(name, result):
        user_results_file = open('user_results.txt', 'a')
        results = [
            UserResultStorage(name, result)
        ]
        user_results_file.write(f'{name:10}{result:15}\n')
        user_results_file.close()
        return results

    def show_user_results():
        name = 'имя'
        result = 'Результат'
        print(f'{name:10}{result:15}')
        user_info_file = open('user_results.txt', 'r')
        return user_info_file.read()


class FileManager():
    def get_info(self):
        user_info_file = open('all_info.txt', 'r')
        return user_info_file.read()

    def add_info(self, info):
        user_info_file = open('all_info.txt', 'a')
        user_info_file.write(info)
        user_info_file.close()

    def change_info(self, info):
        user_info_file = open('all_info.txt', 'w')
        user_info_file.write(info)
        user_info_file.close()


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


# file = open('info.txt', 'a')
while True:

    questions = QuestionStorage.get_questions()
    right_answers_ammount = 0
    qeutions_ammount = len(questions)

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
        random_index = randint(0, len(questions)-1)
        question = questions[random_index].text
        print(i+1, question)
        user_answer = input()
        user_answer = valid_answer_digit(user_answer)
        right_answer = questions[random_index].answer
        if user_answer == right_answer:
            right_answers_ammount += 1
        questions.pop(random_index)
    result = calc_results(qeutions_ammount, right_answers_ammount)
    User.add_user_info(user_name, right_answers_ammount, result)
    UserResultStorage.add_results(user_name, result)
    # resume = [user_name, right_answers_ammount, result, ]
    # resume = " ".join(map(str, resume))
    # print(resume)
    # file.write(resume)
    print('Правильных ответов:', right_answers_ammount)
    print(user_name, ',Вы -', result)
    print('Хотите посмотреть информацию про предыдущих участников? Если хотите введите +, если не хотите введите -')
    answer = input()
    answer = valid_answer_end(answer)
    if answer == '+':
        print(User.show_previous_results())
    print('Хотите посмотреть ирезультаты предыдущих участников? Если хотите введите +, если не хотите введите -')
    answer = input()
    answer = valid_answer_end(answer)
    if answer == '+':
        print(UserResultStorage.show_user_results())
    print('Если хотите сыграть еще раз введите +, если не хотите введите -')
    answer = input()
    answer = valid_answer_end(answer)
    if answer == '+':
        right_answers_ammount = 0
        continue
    else:
        print('Спасибо за участие')
        break
