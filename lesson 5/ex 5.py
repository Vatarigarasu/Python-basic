numbers = input('Введите набор чисел разделенных пробелом: ')
with open('sum.txt', 'w') as file:
    file.write(numbers)
print(sum(map(float, numbers.split())))