def my_func(arg1, arg2):
    return arg1/arg2


arg1 = float(input('Числитель: '))
arg2 = float(input('Знаменатель: '))
print(my_func(arg1, arg2)) if arg2 != 0 else print('ERROR!!! Деление на ноль!')
