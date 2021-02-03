my_list = input('Введите через пробел значения списка: ').split()
odd_list = my_list[::2]
even_list = my_list[1::2]
new_list=[]
i = 0
while i < len(even_list):
    new_list.append(even_list[i])
    new_list.append(odd_list[i])
    i += 1
if len(odd_list) > len(even_list):
    new_list.append(odd_list[i])
print(new_list)
