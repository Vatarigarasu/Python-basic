mesyac = int(input('Номер месяца: '))
# if (mesyac >=1 and mesyac <=12):
#     seasons = dict.fromkeys([1, 2, 12], 'Зима')
#     seasons.update(dict.fromkeys([3, 4, 5], 'Весна'))
#     seasons.update(dict.fromkeys([6, 7, 8], 'Лето'))
#     seasons.update(dict.fromkeys([9, 10, 11], 'Осень'))
#     print(seasons.get(mesyac))
# else:
#     print('Такого месяца не существует')


if (mesyac >=1 and mesyac <=12):
    seasons = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
    print(seasons[mesyac-1])
else:
    print('Такого месяца не существует')

