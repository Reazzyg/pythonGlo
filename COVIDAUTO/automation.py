import os
from attr import validate
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


class Referral:
    def __init__(self, child, anamnez, indications, material, search, doctor, specialist, date_taken, date_send, agreance):
        self.child = child
        self.anamnez = anamnez
        self.indications = indications
        self.material = material
        self.search = search
        self.doctor = doctor
        self.specialist = specialist
        self.date_taken = date_taken
        self.date_send = date_send
        self.agreance = agreance


class ReferralStorage:
    def __init__(self):
        self.file_name = 'referrals.json'

    def get_all(self):
        referrals = []
        data = file_provider.get(self.file_name)
        referrals = jsonpickle.decode(data)
        return referrals

    def save_referrals(self, data):
        json_data = jsonpickle.encode(data)
        file_provider.writelines(self.file_name, json_data)


class Child:
    def __init__(self, name, bday, adress, phone):
        self.name = name
        self.bday = bday
        self.adress = adress
        self.phone = phone


class ChildStorage:
    def __init__(self):
        self.file_name = 'children.json'

    def get_all(self):
        children = []
        if not file_provider.exists(self.file_name):
            print('Введите имя:')
            name = input()
            print('Введите дату рождения:')
            bday = input()
            print('Введите адрес:')
            adress = input()
            print('Введите номер телефона:')
            phone = input()
            children = [
                Child(name, bday, adress, phone)
            ]
            self.save_children(children)
        return children

    def save_children(self, data):
        json_data = jsonpickle.encode(data)
        file_provider.writelines(self.file_name, json_data)

    def add(self, child):
        children = self.get_all()
        children.append(child)
        self.save_children(children)


class Doctor:
    def __init__(self, name):
        self.name = name


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

    def add(self, doctor):
        doctors = self.get_all()
        doctors.append(doctor)
        self.save_doctors(doctors)

    def save_doctors(self, doctors):
        json_data = jsonpickle.encode(doctors)
        file_provider.writelines(self.file_name, json_data)

    def remove(self, index):
        doctors = self.get_all()
        doctors.pop(index)
        self.save_doctors(doctors)


class Specialist:
    def __init__(self, name):
        self.name = name


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

    def add(self, specialist):
        specialists = self.get_all()
        specialists.append(specialist)
        self.save_specialists(specialists)

    def save_specialists(self, specialists):
        json_data = jsonpickle.encode(specialists)
        file_provider.writelines(self.file_name, json_data)

    def remove(self, index):
        specialists = self.get_all()
        specialists.pop(index)
        self.save_specialists(specialists)


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


# def print_children(children):
#     for i in range(len(children)):
#         print(
#             f'{i+1:<10}{children[i].name:<45}')


# def show_all_children(children):
#     number = 'Номер'
#     name = 'Имя'
#     print('--------------------------------------------------------------')
#     print(f'{number:<10}{name:<45}')
#     print_children(children)
#     print('--------------------------------------------------------------')


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

# Создаем бд для детей, если бд нет, то сразу спросит все данные для добавления первого ребенка
while True:
    doctors = doctorStorage.get_all()
    specialists = specialistStorage.get_all()
    childStorage = ChildStorage()
    children = childStorage.get_all()
    add_child()
    print('Введите эпид. анамнез:')
    anamnez = input()
    print('Введите показания для исследования(контингент):')
    indications = input()
    print('Если материал взят при амбулаторном лучении и наблюдении введите "+", если нет - введите "-"')
    material = input()
    print('Выберите врача, назначившего лечение:')
    show_all_doctors(doctors)
    doctor_index = input()
    print('Выберите специалиста, осуществляющего забор биоматериала:')
    show_all_specialists(specialists)
    spesialist_index = input()
