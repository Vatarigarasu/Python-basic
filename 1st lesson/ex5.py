income = int(input('Введите вашу выручку: '))
credit = int(input('Введите ваши издержки: '))
if credit > income:
    print('Мы теряем деньги, Милорд')
elif credit < income:
    print('Наша казна растет')
    profit = income - credit
    rent = profit / income
    workers = int(input('Введите число сотрудников: '))
    ProfitPerWorker = profit / workers
    print(f'Наша прибыль составила {profit}, рентабильность при этом составила {rent}. '
          f'Прибыль в пересчете на каждого сотрудника составила {ProfitPerWorker}')
else:
    print('Мы вышли в ноль')
