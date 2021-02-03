my_list = input('Введите через пробел значения списка: ').split()
i = 1
for box in my_list:
    print(i, ') ', box[:9], sep='')
    i += 1
