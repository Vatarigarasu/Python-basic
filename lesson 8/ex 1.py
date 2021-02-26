# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
# числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class DataError(Exception):
    def __init__(self, msg):
        self.msg = msg
        print('Попробуйте ввести другую дату')


class Data:

    def __init__(self, data):
        self.data = str(self.morph(data))
        self.data_check(data)
        self.morph(data)

    @classmethod
    def morph(cls, data):
        return data.split('-')

    @staticmethod
    def data_check(data):
        calendar = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        validated_data = Data.morph(data)
        if int(validated_data[1]) not in calendar.keys():
            raise DataError('Такого месяца нет')
        # из ТЗ непонятно какие года являются валидными, и я так и не смог разобраться как устроен високосный год
        # по Григорианскому календарю поэтому не стал добавлять 29 февраля
        print('Month: OK')
        if 0 < int(validated_data[0]) > calendar[int(validated_data[1])]:
            raise DataError('30 дней всегда в сентябре, \n'
                                'В апреле, июне и ноябре.\n'
                                'На день больше в месяцах прочих,\n'
                                'Только февраль подравняться не хочет.\n'
                                'В нём всего 28 дней,\n'
                                'Но в год високосный он на день длинней!')
        print('Day: OK')
        if not 1890 < int(validated_data[2]) < 2050:
            raise DataError('Вам правда нужны такие далекие даты?')
        print('Year: OK')


special_day = Data('14-02-2021')
print(special_day.data)
