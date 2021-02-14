# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.

with open('persons.txt', 'r', encoding='utf-8') as f:
    FOT = 0
    poors = []
    counter = 0
    for i in f:
        counter += 1
        a = i.split()
        FOT += float(a[1])
        if float(a[1]) < 20000.0:
            poors.append(a[0])

print(f'Бедные сотрудники: {", ".join(i for i in poors)}\nСредняя зарплата: {FOT/counter}')
