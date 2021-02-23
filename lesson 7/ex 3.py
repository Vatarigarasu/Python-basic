class Cell:

    def __init__(self, bin_number):
        self.bin_number = int(bin_number)

    def __add__(self, other):
        try:
            return self.bin_number + other.bin_number
        except AttributeError:
            return 'Что-то не так'

    def __sub__(self, other):
        try:
            return self.bin_number - other.bin_number
        except AttributeError:
            return 'Что-то не так'

    def __mul__(self, other):
        try:
            return self.bin_number * other.bin_number
        except AttributeError:
            return 'Что-то не так'

    def __truediv__(self, other):
        try:
            return self.bin_number // other.bin_number
        except AttributeError:
            return 'Что-то не так'

    def make_order(self, bin_length):
        bins = self.bin_number // bin_length
        tail = self.bin_number % bin_length
        return bins*(bin_length*'*'+'\n') + tail*'*'


a = Cell(3)
b = Cell(7)
c = Cell(15)

print(a + b)
print(b - a)
print(b * a)
print(b / a)

print(b.make_order(4))
print(c.make_order(5))