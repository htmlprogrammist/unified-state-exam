"""
Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт.
Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
В строках, содержащих менее 25 букв G,
нужно определить и вывести максимальное расстояние между одинаковыми буквами в одной строке.
Пример. Исходный файл:
GIGA
GABLAB
NOTEBOOK
AGAAA
В этом примере во всех строках меньше 25 букв G.
Самое большое расстояние между одинаковыми буквами – в третьей строке между буквами O,
расположенными в строке на 2-й и 7-й позициях. В ответе для данного примера нужно вывести число 5.
"""
document = open('24.txt')
a = document.readlines()
distance = 0
max_distance = 0

for i in range(len(a)):
    if a[i].count('G') < 25:
        for j in range(len(a[i])):
            while 
