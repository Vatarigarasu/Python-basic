my_list = [7, 5, 3, 3, 2]
while True:
    print('Текущий Рейтинг:', my_list)
    new = input('Введите новое значения рейтинга или напишите слово "стоп", чтобы закончить: ')
    if new == 'стоп':
        break
    my_list.append(int(new))
    my_list.sort(reverse=True)

