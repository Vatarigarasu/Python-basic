a = int(input('Начальная дистанция: '))
b = int(input('Конечная дистанция: '))
day = 1

while a < b:
    a *= 1.1
    day += 1

print(f'На {day} день спортсмен достиг результат {b} км.')
