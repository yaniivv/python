# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

A = (input ('Введите номер четверти: '))
if A == '1':
    print('I четверть включает все числа где, x > 0, y > 0')
if A == '2':
    print('II четверть включает все числа где, x < 0, y > 0')
if A == '3':
    print('III четверть включает все числа где, x < 0, y < 0')
if A == '4':
    print('IV четверть включает все числа где, x > 0, y < 0')