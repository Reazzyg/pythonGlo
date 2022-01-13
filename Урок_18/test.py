from random import randint
import os


class FileManager:
    def get(self, path):
        file = open(path, 'r')
        data = file.read()
        file.close()
        return data

    def add(self, path, info):
        user_info_file = open(path, 'a')
        user_info_file.write(info)
        user_info_file.close()

    def exists(self, path):
        return os.path.exists(path)

    def clear(self, path):
        file = open(path, 'w')
        data = file.write('')
        file.close


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class QuestionStorage:
    def get_all(self):
        file_name = 'Урок_18/questions.txt'
        if not file_provider.exists(file_name):
            questions = [
                Question('вопрос 1', 1),
                Question('вопрос 2', 2),
                Question('вопрос 3', 3),
                Question('вопрос 4', 4),
                Question('вопрос 5', 5),
                Question('вопрос 6', 6),
                Question('вопрос 7', 7),
                Question('вопрос 8', 8),
                Question('вопрос 9', 9),
                Question('вопрос 10', 10),
                Question('вопрос 11', 11),
                Question('вопрос 12', 12),

            ]
            self.save_questions(questions)
        data = file_provider.get(file_name).strip('\n')
        data = data.split('\n')
        questions = []
        for line in data:
            values = line.split('#')
            question = Question(values[0], int(values[1]))
            questions.append(question)
        return questions

    def save_questions(self, questions):
        for question in questions:
            self.add(question)

    def add(self, question):
        file_name = 'Урок_18/questions.txt'
        data = f'{question.text}#{question.answer}\n'
        file_provider.add(file_name, data)

    def remove(self, index):
        questions = self.get_all()
        questions.pop(index)

        file_name = 'Урок_18/questions.txt'
        file_provider.clear(file_name)

        self.save_questions(questions)


class User:
    def __init__(self, name, right_answers_ammount=0, result='unknown'):
        self.name = name
        self.right_answers_ammount = right_answers_ammount
        self.result = result

    def accept_right_result(self):
        self.right_answers_ammount += 1

    def set_result(self, result):
        self.result = result


class UserResultStorage:
    def save(self, user):
        file_name = 'Урок_18/results.txt'
        file_provider = FileManager()
        data = f'{user.name}#{user.result}#{user.right_answers_ammount}\n'
        file_provider.add(file_name, data)

    def get_all(self):
        file_name = 'Урок_18/results.txt'
        file_provider = FileManager()
        data = file_provider.get(file_name).strip('\n')
        data = data.split('\n')
        users = []
        for line in data:
            values = line.split('#')
            user = User(values[0], values[1], values[2])
            users.append(user)
        return users
    # def __init__(self, name, result):
    #     self.name = name
    #     self.result = result

    # def add_results(name, result):
    #     user_results_file = open('user_results.txt', 'a')
    #     results = [
    #         UserResultStorage(name, result)
    #     ]
    #     user_results_file.write(f'{name:10}{result:15}\n')
    #     user_results_file.close()
    #     return results

    # def show_user_results():
    #     name = 'имя'
    #     result = 'Результат'
    #     print(f'{name:10}{result:15}')
    #     user_info_file = open('results.txt', 'r')
    #     return user_info_file.read()


def print_questions(questions):
    print('------------------------------------------')
    for i in range(len(questions)):
        print(f'{i+1}.{questions[i].text}')
    print('------------------------------------------')


def remove_question():
    questions = questionsStorage.get_all()
    while True:
        print('Выберите номер вопроса, который надо удалить')
        print_questions(questions)
        user_answer = input()
        user_answer = valid_answer_digit(user_answer)
        if user_answer < 1 or user_answer > len(questions):
            continue
        questionsStorage.remove(user_answer-1)
        print(f'вопрос под номером {user_answer} успешно удален')
        break


def add_new_question():
    print('введите текст вопроса')
    text = input()
    print('ввдети ответ на вопрос')
    answer = input()
    answer = valid_answer_digit(answer)
    new_question = Question(text, answer)
    questionsStorage.add(new_question)


def show_user_results():
    name = 'имя'
    result = 'Результат'
    right_answers_ammount = 'Кол-во правильных ответов'
    print(f'{name:10}{result:15}{right_answers_ammount:25}')
    users = userResultStorage.get_all()
    for user in users:
        print(f'{user.name:10}{user.result:15}{user.right_answers_ammount:25}')


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


file_provider = FileManager()
questionsStorage = QuestionStorage()
userResultStorage = UserResultStorage()
# file = open('info.txt', 'a')
while True:

    questions = questionsStorage.get_all()
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
    user = User(user_name)
    for i in range(len(questions)):
        random_index = randint(0, len(questions)-1)
        question = questions[random_index].text
        print(i+1, question)
        user_answer = input()
        user_answer = valid_answer_digit(user_answer)
        right_answer = questions[random_index].answer
        if user_answer == right_answer:
            user.accept_right_result()
        questions.pop(random_index)
    result = calc_results(qeutions_ammount, user.right_answers_ammount)
    user.set_result(result)

    userResultStorage.save(user)

    print('Правильных ответов:', user.right_answers_ammount)
    print(user_name, ',Вы -', result)
    print('Хотите добавиьт вопрос? Если хотите введите +, если не хотите введите -')
    answer = input()
    answer = valid_answer_end(answer)
    if answer == '+':
        add_new_question()
    print('Хотите удалить вопрос? Если хотите введите +, если не хотите введите -')
    answer = input()
    answer = valid_answer_end(answer)
    if answer == '+':
        remove_question()
    print('Хотите посмотреть информацию про предыдущих участников? Если хотите введите +, если не хотите введите -')
    answer = input()
    answer = valid_answer_end(answer)
    if answer == '+':
        show_user_results()
    print('Если хотите сыграть еще раз введите +, если не хотите введите -')
    answer = input()
    answer = valid_answer_end(answer)
    if answer == '+':
        right_answers_ammount = 0
        continue
    else:
        print('Спасибо за участие')
        break
