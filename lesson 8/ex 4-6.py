# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который
# будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
# классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры, уникальные для
# каждого типа оргтехники.
# Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу
# в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру (например, словарь).
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
# указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
from prettytable import PrettyTable
a = PrettyTable()
a.field_names = ['№ п/п', 'Наименование', 'Тип устройства']


class Warehouse:
    store = {}

    @classmethod
    def __str__(cls):
        return f' Распределение оргтехники: {cls.store}'

    @classmethod
    def put_in(cls, objects, quantity):
        if objects.name not in cls.store:
            cls.store[objects.name] = {'store': quantity}
        else:
            cls.store[objects.name]['store'] += quantity

    @classmethod
    def put_off(cls, objects, direction, quantity):
        if objects.name not in cls.store:
            print('На складе отсутствует эта позиция')
        elif cls.store[objects.name]['store'] < quantity:
            print('На складе недостаточно этой техники')
        else:
            cls.store[objects.name]['store'] -= quantity
            print(cls.store[objects.name].keys())
            if direction not in cls.store[objects.name].keys():
                cls.store[objects.name].update({direction: quantity})
            else:
                cls.store[objects.name][direction] += quantity


class OfficeEquipment:
    def __init__(self, speed, paper_format, name):
        self.speed = speed
        self.paper_format = paper_format
        self.name = name


class Printer(OfficeEquipment):
    def __init__(self, color_scheme, printer_type, speed, paper_format, name):
        super().__init__(speed, paper_format, name)
        self.color_scheme = color_scheme
        self.type = printer_type

    def __str__(self):
        return self.name


class Scanner(OfficeEquipment):
    def __init__(self, resolution, speed, paper_format, name):
        super().__init__(speed, paper_format, name)
        self.resolution = resolution

    def __str__(self):
        return self.name


class Shredder(OfficeEquipment):
    def __init__(self, security_standard, lists, speed, paper_format, name):
        super().__init__(speed, paper_format, name)
        self.security_standard = security_standard
        self.lists = lists

    def __str__(self):
        return self.name


# Box1 = Printer('RGB', 'Inkjet', 15, 'A4', 'HP 640')
# Box2 = Scanner(4800, 6, 'A4', 'Epson Perfection V19')
# Box3 = Shredder(4, 8, 10, 'A4', 'Brauberg S8')
# Warehouse.put_in(Box1, 10)
# Warehouse.put_in(Box2, 20)
# Warehouse.put_in(Box3, 5)
warehouse = Warehouse()
# print(warehouse)
# Warehouse.put_in(Box1, 5)
# print(warehouse)
# Warehouse.put_off(Box1, 'Office', 40)
# Warehouse.put_off(Box1, 'Office', 4)
# Warehouse.put_off(Box1, 'Office', 8)
# print(warehouse)

# дойдя до третьего пункта задания пошел в разнос

boxes = []
while True:
    case = input('[1] - добавить новую позицию в базу \n[2] - добавить какое-то количество '
                 'техники на склад \n[3] - перенести куда-либо какое-либо количество техники.'
                 '\n[4] - список известных устройств \nДля выхода из программы введете "STOP" \n Выберете действие: ')
    if case == 'STOP':
        break
    if case.find('1') != -1:
        device = input('[1] - принтер \n[2] - сканер \n[3] - шредер \nВыберете типа устройства: ')
        Parameters = [input('Скорость: '), input('Формат страницы: '), input('Наименование устройства: ')]
        if device.find('1') != -1:
            Parameters.insert(0, input('Тип принтера: '))
            Parameters.insert(0, input('Цветовая схема: '))
            boxes.append(Printer(*Parameters))
            a.add_row([len(boxes), boxes[-1].name, 'Принтер'])
        elif device.find('2') != -1:
            Parameters.insert(0, input('Разрешение сканера: '))
            boxes.append(Scanner(*Parameters))
            a.add_row([len(boxes), boxes[-1].name, 'Сканер'])
        elif device.find('3') != -1:
            Parameters.insert(0, input('Число единовременно уничтожаемых страниц: '))
            Parameters.insert(0, input('Стандарт безопасности: '))
            boxes.append(Shredder(*Parameters))
            a.add_row([len(boxes), boxes[-1].name, 'Шрёдер'])
        print(f'Новое устройство {boxes[-1]}')
        try:
            quantity1 = input('Сколько положить на склад? ')
            if not quantity1.isdigit():
                raise TypeError('ERROR! Неверные данные')
            quantity1 = int(quantity1)
        except TypeError:
            quantity1 = input('Вы ввели что-то другое, попробуйте ввести число. Сколько положить на склад? ')

        Warehouse.put_in(boxes[-1], quantity1)
        print(warehouse)
    elif case.find('2') != -1:
        i = int(input('Какую позицию добавляем на склад? '))
        Warehouse.put_in(boxes[i-1], int(input('Сколько положить на склад? ')))
        print(warehouse)
    elif case.find('3') != -1:
        i = int(input('Какую позицию отгружаем со склада?'))
        Warehouse.put_off(boxes[i-1], input('Куда отгрузить? '), int(input('Сколько отгрузить? ')))
        print(warehouse)
    elif case.find('4') != -1:
        print(a)
