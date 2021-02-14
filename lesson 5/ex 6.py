# Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и
# наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.

numbers = [str(_) for _ in range(10)]
numbers.append(' ')
my_dict={}

with open('lessons.txt', 'r', encoding='utf-8') as file:
    for line in file:
        filtered_string = filter(lambda i: i in numbers, line)
        filtered_string = "".join(filtered_string)
        hours = sum([int(i) for i in filtered_string.split(' ') if i != ''])
        key = line.split(' ')[0]
        my_dict[key] = hours

print(my_dict)
