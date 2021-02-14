# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл
# не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором
# также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count, cycle

first_el = int(input('Введите целое стартовое цисло: '))

pause_counter = 0
for i in count(first_el):
    print(i)
    if pause_counter == 0:
        key = input("Сколько сгенерировать чисел? [Введите целое положительное число или Q чтобы закончить]: ").upper()
        if key == 'Q':
            break
        try:
            pause_counter = int(key)
        except ValueError:
            print('Введено неверное значение. Необходимо вводить целые положительные числа:')
            break
    pause_counter -= 1

string = 'lorem_ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore ' \
         'et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut ' \
         'aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum ' \
         'dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui ' \
         'officia deserunt mollit anim id est laborum.'.split(' ')

for el in cycle(string):
    print(el)
    if pause_counter == 0:
        key = input("Сколько сгенерировать слов? [Введите целое положительное число или Q чтобы закончить]: ").upper()
        if key == 'Q':
            break
        try:
            pause_counter = int(key)
        except ValueError:
            print('Введено неверное значение. Необходимо вводить целые положительные числа:')
            break
    pause_counter -= 1
