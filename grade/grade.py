import os
from xml.etree.ElementTree import TreeBuilder
import jsonpickle


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
        file.write('')
        file.close

    def writelines(self, path, data):
        file = open(path, 'w')
        data = file.writelines(data)
        file.close()


class School:
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress


class SchoolStorage:
    def __init__(self):
        self.file_name = 'grade/school.json'

    def get_all(self):
        school_info = []
        if not file_provider.exists(self.file_name):
            print('Введите название школы')
            self.name = input()
            # school_info = school_info.append(self.name)
            print('Введите адрес школы')
            self.adress = input()
            # school_info = school_info.append(self.adress)
            school_info = [School(self.name, self.adress)]
            self.save_school_info(school_info)
        data = file_provider.get(self.file_name)
        school_info = jsonpickle.decode(data)
        return school_info

    def save_school_info(self, data):
        json_data = jsonpickle.encode(data)
        file_provider.writelines(self.file_name, json_data)

    def remove(self, index):
        school_info = self.get_all()
        school_info.pop(index)
        self.save_school_info()

    def rename(self, name):
        school_info = self.get_all()
        adress = school_info[0].adress
        school_info = [School(name, adress)]
        self.save_school_info(school_info)

    def readress(self, adress):
        school_info = self.get_all()
        name = school_info[0].name
        school_info = [School(name, adress)]
        self.save_school_info(school_info)


class Student:
    def __init__(self,  name, age, class_name):
        self.name = name
        self.age = age
        self.class_name = class_name


class StudentsStorage:

    def __init__(self):
        self.file_name = 'grade/students.json'

    def get_all(self):
        if not file_provider.exists(self.file_name):
            students = [
                Student('Мудров Семен Александрович', 16, '9a'),
                Student('Мудров Евгений Александрович', 15, '8г'),
                Student('Мудров Александр Александрович', 17, '10б'),
                Student('Мудров Леонид Александрович', 13, '6a'),
                Student('Мудров Антон Александрович', 10, '3')
            ]
            self.save_students(students)
        data = file_provider.get(self.file_name)
        students = jsonpickle.decode(data)
        return students

    def add(self, student):
        students = self.get_all()
        students.append(student)
        self.save_students(students)

    def save_students(self, students):
        json_data = jsonpickle.encode(students)
        file_provider.writelines(self.file_name, json_data)

    def remove(self, index):
        students = self.get_all()
        students.pop(index)
        self.save_students(students)


def calc_students(students):
    student_ammount = len(students)
    return student_ammount


def print_menu():
    print('1. Получить полную информацию о школе')
    print('2. Изменить информацию о школе')
    print('3. Просмотреть учеников школы')
    print('4. Добавить нового ученика')
    print('5. Удалить ученика')
    print('6. Выйти из программы')


def show_school_info(school):
    print(f'Название школы: {school[0].name}')
    print(f'Адрес школы: {school[0].adress}')
    print(f'Количество учеников: {calc_students(students)}')


def add_new_student():
    print('Введите ФИО')
    student_name = input()
    print('Введите Возраст')
    student_age = input()
    student_age = valid_answer(student_age)
    print('Введите Номер класса')
    student_class = input()
    new_student = Student(student_name, student_age, student_class)
    studentsStorage.add(new_student)


def print_students(students):
    for i in range(len(students)):
        print(
            f'{i+1:<10}{students[i].name:<45}{students[i].age:<10}{students[i].class_name:<10}')


def show_all_students(students):
    number = 'Номер'
    name = 'Имя'
    age = 'Возраст'
    student_class = 'Класс'
    print('--------------------------------------------------------------')
    print(f'{number:<10}{name:<45}{age:<10}{student_class:<10}')
    print_students(students)
    print('--------------------------------------------------------------')


def remove_student(students):
    students = studentsStorage.get_all()
    while True:
        print('--------------------------------------------------------------')
        print('Выберите номер ученика, которого надо удалить')
        print_students(students)
        print('--------------------------------------------------------------')
        user_answer = input()
        user_answer = valid_answer_digit(user_answer)
        if user_answer < 1 or user_answer > len(students):
            continue
        studentsStorage.remove(user_answer-1)
        print(f'Ученик под номером {user_answer} успешно удален')
        break


def valid_answer(answer):
    while True:
        if answer.isdigit():
            answer = int(answer)
            break
        else:
            print('Ответ должен состоять из цифр')
            answer = input()
            continue
    return answer


def valid_answer_digit(answer):
    while True:
        if answer.isdigit():
            answer = int(answer)
            break
        else:
            print('Введить число от 1 до 6')
            answer = input()
            continue
    return answer


jsonpickle.set_encoder_options(
    'json', indent=4, separators=(',', ': '), ensure_ascii=False)
file_provider = FileManager()
schoolStorage = SchoolStorage()
studentsStorage = StudentsStorage()
while True:
    students = studentsStorage.get_all()
    students_ammuont = calc_students(students)
    school_info = schoolStorage.get_all()
    print('Меню')
    print_menu()
    print('Выберите пункт меню')
    answer = input()
    answer = valid_answer_digit(answer)
    if answer == 1:
        show_school_info(school_info)
    if answer == 2:
        print('--------------------------------------------------------------')
        print('1. Изменить название школы')
        print('2. Изменить адрес школы')
        print('3. Вернуться обратно')
        print('--------------------------------------------------------------')
        answer = input()
        answer = valid_answer_digit(answer)
        if answer == 1:
            print('Введите новое название школы')
            school_name = input()
            schoolStorage.rename(school_name)
        if answer == 2:
            print('Введите новый адрес школы')
            school_adress = input()
            schoolStorage.readress(school_adress)
        if answer == 3:
            continue
    if answer == 3:
        show_all_students(students)
    if answer == 4:
        add_new_student()
    if answer == 5:
        remove_student(students)
    if answer == 6:
        print('Вы вышли из программы')
        break
