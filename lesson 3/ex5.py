def my_func(args, old=0):
    return sum([*args, old])


string = input('Введите последовательность чисел разделенных пробелом, для вычисления их суммы:').split(' ')
int_string = [int(x) for x in string]
res = my_func(int_string)
print(res)
while True:
    string = input('Напишите "Q" чтобы выйти или продолжайте вводить числа через пробел:').upper()
    if string == 'Q':
        break
    else:
        int_string = [int(x) for x in string.split(' ')]
        res = my_func(int_string, old=res)
        print(res)
