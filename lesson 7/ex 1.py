from random import randint


class Matrix:
    def __init__(self, array):
        self.array = array

    def __str__(self):
        MyStr = ''
        for i in range(len(self.array)):
            for j in range(len(self.array[0])):
                MyStr += f'{self.array[i][j]:>4}'
            MyStr += '\n'
        return MyStr

    def __add__(self, other):
        return Matrix([[self.array[j][i]+other.array[j][i] for i in range(m)] for j in range(n)])


m = randint(1, 5)
n = randint(1, 5)
array1 = [[randint(-10, 10) for i in range(m)] for j in range(n)]
array2 = [[randint(-10, 10) for i in range(m)] for j in range(n)]
A = Matrix(array1)
print(A)
B = Matrix(array2)
print(B)
C = A + B
print(C)
