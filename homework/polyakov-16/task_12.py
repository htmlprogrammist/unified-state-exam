"""
(№ 2121) Исполнитель Редактор получает на вход строку цифр и преобразовывает её.
Редактор может выполнять две команды, в обеих командах v и w обозначают цепочки цифр.
1. заменить (v, w)
2. нашлось (v)
Первая команда заменяет в строке первое слева вхождение цепочки v на цепочку w.
Если цепочки v в строке нет, эта команда не изменяет строку. Вторая команда проверяет,
встречается ли цепочка v в строке исполнителя Редактор. Если она встречается,
то команда возвращает логическое значение «истина», в противном случае возвращает значение «ложь».
Дана программа для исполнителя Редактор:
НАЧАЛО
  ПОКА нашлось (777)
    заменить (777, 22)
    заменить (222, 7)
  КОНЕЦ ПОКА
КОНЕЦ
Какая строка получится в результате применения приведённой ниже программы к строке, состоящей из 143 цифр 7?

22
"""
s = 143 * '7'
while '777' in s:
    s = s.replace('777', '22', 1)
    s = s.replace('222', '7', 1)
print(s)