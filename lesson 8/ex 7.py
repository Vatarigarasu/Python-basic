# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f'{self.real}+i*{self.imaginary}'

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber((self.real * other.real - self.imaginary * other.imaginary),
                             (self.real * other.imaginary + self.imaginary * other.real))


a = ComplexNumber(4, 3)
print(a)
b = ComplexNumber(3, 5)
print(b)
c = a + b
print(c)
d = a * b
print(d)
