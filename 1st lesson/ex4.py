num = int(input('Введите целое положительное число: '))
Biggest = 0

while True:
    buff = num % 10
    num //= 10
    if buff > Biggest:
        Biggest = buff
    if num == 0:
        break

print(Biggest)
