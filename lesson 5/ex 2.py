# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open('lorem_ipsum.txt', 'r') as f:
    lines, words, all_words = 0, 0, 0
    for string in f:
        lines += 1
        words = len(string.split(' '))
        print(f'Строка {lines} содержит {words} слов')
        all_words += words
print(f'Итого {all_words} слов в {lines} строках')
