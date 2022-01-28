import os
from re import search
from time import time
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

# Создаем объект "направление"


class Referral:
    def __init__(self, name, bday, adress, phone, anamnez, indications, material, time, doctor, specialist, date_taken, date_send, agreance):
        self.name = name
        self.bday = bday
        self.adress = adress
        self.phone = phone
        self.anamnez = anamnez
        self.indications = indications
        self.material = material
        self.time = time
        self.doctor = doctor
        self.specialist = specialist
        self.date_taken = date_taken
        self.date_send = date_send
        self.agreance = agreance

# Создаем хранилище направлений, возможность их сохранять и добавлять в хранилище


class ReferralStorage:
    def __init__(self):
        self.file_name = 'referrals.json'

    def get_all(self):
        referrals = []
        if not file_provider.exists(self.file_name):
            child = add_child()
            add_referral(child.name, child.bday, child.adress, child.phone)
        data = file_provider.get(self.file_name)
        referrals = jsonpickle.decode(data)
        return referrals

    def save_referrals(self, data):
        json_data = jsonpickle.encode(data)
        file_provider.writelines(self.file_name, json_data)

    def add(self, referral):
        referrals = self.get_all()
        referrals.append(referral)
        self.save_referrals(referrals)

# создаем объект "ребенок"


class Child:
    def __init__(self, name, bday, adress, phone):
        self.name = name
        self.bday = bday
        self.adress = adress
        self.phone = phone

# создаем хранилище детей


class ChildStorage:
    def __init__(self):
        self.file_name = 'children.json'

    def get_all(self):
        children = []
        data = file_provider.get(self.file_name)
        children = jsonpickle.decode(data)
        return children
# сохранение детей

    def save_children(self, data):
        json_data = jsonpickle.encode(data)
        file_provider.writelines(self.file_name, json_data)
# добавление детей в хранилище

    def add(self, child):
        children = self.get_all()
        children.append(child)
        self.save_children(children)

# создаем объект врач


class Doctor:
    def __init__(self, name):
        self.name = name

# создаем хранилище врачей


class DoctorStorage:
    def __init__(self):
        self.file_name = 'doctors.json'

    def get_all(self):
        if not file_provider.exists(self.file_name):
            print('Введите ФИО врача')
            self.name = input()
            doctors = [
                Doctor(self.name)
            ]
            self.save_doctors(doctors)
        data = file_provider.get(self.file_name)
        doctors = jsonpickle.decode(data)
        return doctors
# добавляем врача

    def add(self, doctor):
        doctors = self.get_all()
        doctors.append(doctor)
        self.save_doctors(doctors)
# созхраняем

    def save_doctors(self, doctors):
        json_data = jsonpickle.encode(doctors)
        file_provider.writelines(self.file_name, json_data)
# убрать врача

    def remove(self, index):
        doctors = self.get_all()
        doctors.pop(index)
        self.save_doctors(doctors)

# создаем объект сепциалист


class Specialist:
    def __init__(self, name):
        self.name = name

# создаем хранилище специалистов


class SpecialistStorage:
    def __init__(self):
        self.file_name = 'specialists.json'

    def get_all(self):
        if not file_provider.exists(self.file_name):
            print('Введите ФИО специалиста')
            self.name = input()
            specialists = [
                Specialist(self.name)
            ]
            self.save_specialists(specialists)
        data = file_provider.get(self.file_name)
        specialists = jsonpickle.decode(data)
        return specialists
# добавление специалистов

    def add(self, specialist):
        specialists = self.get_all()
        specialists.append(specialist)
        self.save_specialists(specialists)
# сохранение специалистов

    def save_specialists(self, specialists):
        json_data = jsonpickle.encode(specialists)
        file_provider.writelines(self.file_name, json_data)
# убрать специалиста

    def remove(self, index):
        specialists = self.get_all()
        specialists.pop(index)
        self.save_specialists(specialists)

# добавляем нового ребенка в бд


def add_child():
    print('Введите имя ребенка:')
    name = input()
    print('Введите дату рождения:')
    bday = input()
    print('Введите адрес:')
    adress = input()
    print('Введите номер телефона:')
    phone = input()
    new_child = Child(name, bday, adress, phone)
    childStorage.add(new_child)
    return new_child

# добавляем новое направление в бд


def add_referral(name, bday, adress, phone):
    print('Введите эпид. анамнез:')
    anamnez = input()
    print('Введите показания для исследования(контингент):')
    indications = input()
    material = "+"
    print('Если обследование на COVID-19 проводится впервые введите "+", если нет - введите "-"')
    time = input()
    doctor = choose_doctor(doctors)
    specialist = choose_specialist(specialists)
    print('Введите дату забора биоматериала')
    date_taken = date_send = input()
    agreance = 'Получено согласие пациента на передачу в страховую медицинскую организацию и обработку информации о результатха тестирования на новую коронавирусню инфекцию из лабораторий, осуществляющих ПЦР, и отправку страховой медицинской организацией смс-уведомления о результате тестирования'
    new_referral = Referral(name, bday, adress, phone,
                            anamnez, indications, material, time, doctor, specialist, date_taken, date_send, agreance)
    referralStorage.add(new_referral)

#  выбираем нужного врача из доступного списка(бд)


def choose_doctor(doctors):
    print('Выберите врача, назначившего лечение:')
    show_all_doctors(doctors)
    doctor_index = int(input())
    doctor = doctors[doctor_index - 1].name
    return doctor

# выбираем нужного специалиста из доступного списка(бд)


def choose_specialist(specialists):
    print('Выберите специалиста, осуществляющего забор биоматериала:')
    show_all_specialists(specialists)
    specialist_index = int(input())
    specialist = specialists[specialist_index-1].name
    return specialist

# вывод всех врачей


def print_doctors(doctors):
    for i in range(len(doctors)):
        print(
            f'{i+1:<10}{doctors[i].name:<45}')


def show_all_doctors(doctors):
    number = 'Номер'
    name = 'Имя'
    print('--------------------------------------------------------------')
    print(f'{number:<10}{name:<45}')
    print_doctors(doctors)
    print('--------------------------------------------------------------')

# вывод всех специалистов


def print_specialists(specialists):
    for i in range(len(specialists)):
        print(
            f'{i+1:<10}{specialists[i].name:<45}')


def show_all_specialists(specialists):
    number = 'Номер'
    name = 'Имя'
    print('--------------------------------------------------------------')
    print(f'{number:<10}{name:<45}')
    print_specialists(specialists)
    print('--------------------------------------------------------------')


def validate_digit(answer):
    while True:
        if answer.isdigit():
            answer = int(answer)
            break
        else:
            print('Введите число')
            answer = input()
            continue
    return answer


jsonpickle.set_encoder_options(
    'json', indent=4, separators=(',', ': '), ensure_ascii=False)
file_provider = FileManager()
doctorStorage = DoctorStorage()
specialistStorage = SpecialistStorage()


doctors = doctorStorage.get_all()
specialists = specialistStorage.get_all()

# Выводим всех врачей, если требуется - добавляем еще
show_all_doctors(doctors)
print('Если требуется добавить врачей введите "+", если нет - введите "-"')
answer = input()
if answer == '+':
    print('Введите количество врачей:')
    doctors_ammount = input()
    doctors_ammount = validate_digit(doctors_ammount)
    for i in range(doctors_ammount):
        print('Введите ФИО врача')
        doctor_name = input()
        new_doctor = Doctor(doctor_name)
        doctorStorage.add(new_doctor)


# Выводим всех специалистов, если требуется - добавляем еще
show_all_specialists(specialists)
print('Если требуется добавить специалистов введите "+", если нет - введите "-"')
answer = input()
if answer == '+':
    print('Введите количество специалистов:')
    specialists_ammount = input()
    specialists_ammount = validate_digit(specialists_ammount)
    for i in range(specialists_ammount):
        print('Введите ФИО специалиста')
        specialist_name = input()
        new_specialist = Specialist(specialist_name)
        specialistStorage.add(new_specialist)


# Создаем бд для детей
childStorage = ChildStorage()
children = childStorage.get_all()

# Создаем бд направлений, при первом запуске будет создано первое направление
referralStorage = ReferralStorage()

while True:
    doctors = doctorStorage.get_all()
    specialists = specialistStorage.get_all()
    children = childStorage.get_all()
    referrals = referralStorage.get_all()
    child = add_child()
    add_referral(child.name, child.bday, child.adress, child.phone)
