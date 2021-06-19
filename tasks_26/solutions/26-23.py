# Автор: А.Н. Носкин
""" Идея:
считываем все результаты в массив, сортируем их по убыванию.
Определяем последний результат победителя и призера
"""
with open("26-3k.txt") as F:
  n, k, m = map(int, F.readline().split()) # строку файла превращаем в 3 числа
# n  - общее кол-во участников
# k -  кол-во победителей
# m -  кол-во призеров

  a = [] # массив хранения всех измерений
  for i in range(n):
    rez = F.readline()  # очередной результат
    a.append(int(rez)) #  число и добавили в массив

  a.sort(reverse = True)
  print(a[k+m-1],a[k-1])


