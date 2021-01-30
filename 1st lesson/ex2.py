Seconds = int(input('Число секунд: '))
Hours = Seconds // 3600
Minutes = Seconds % 3600 // 60
LastSeconds = Seconds % 3600 % 60

if Minutes<10:
    Minutes = '0' + str(Minutes)
if Hours < 10:
    Hours = '0' + str(Hours)
if LastSeconds<10:
    LastSeconds = '0' + str(LastSeconds)

print(f'{Hours}:{Minutes}:{LastSeconds}')
