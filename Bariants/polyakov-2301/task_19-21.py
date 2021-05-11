"""
(№ 2423) Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежат две кучи камней.
Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может добавить
в одну из куч один камень или увеличить количество камней в куче в два раза.
Чтобы делать ходы, у каждого игрока есть неограниченное количество камней.
Игра завершается в тот момент, когда суммарное количество камней в кучах становится не менее 49.
Победителем считается игрок, сделавший последний ход, т. е. первым получивший позицию,
в которой в кучах будет 49 или больше камней.
В начальный момент в первой куче было 7 камней, во второй куче – S камней, 1 ≤ S ≤ 41.
Будем говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах противника.
Ответьте на следующие вопросы:
  Вопрос 1. Известно, что Ваня выиграл своим первым ходом после неудачного первого хода Пети.
  Назовите минимальное значение S, при котором это возможно.
  Вопрос 2. Найдите два таких значения S, при которых у Пети есть выигрышная стратегия,
  причём Петя не может выиграть первым ходом, но может выиграть своим вторым ходом независимо от того,
  как будет ходить Ваня. Найденные значения запишите в ответе в порядке возрастания.
  Вопрос 3. Сколько существует значений S, при которых у Вани есть выигрышная стратегия,
  позволяющая ему выиграть первым или вторым ходом при любой игре Пети,
  и при этом у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.

11
17 20
2
"""
from functools import *


def moves(h):
    a, b = h
    return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 2)


@lru_cache(None)
def game(h):
    a, b = h
    if a + b >= 49:
        return 'W'

    if any(game(m) == 'W' for m in moves(h)):
        return 'P1'
    # if any(game(m) == 'P1' for m in moves(h)):  # для 19 задания
    if all(game(m) == 'P1' for m in moves(h)):
        return 'V1'
    if any(game(m) == 'V1' for m in moves(h)):
        return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)):
        return 'V2'


for s in range(1, 41 + 1):
    h = 7, s
    print(s, game(h))
