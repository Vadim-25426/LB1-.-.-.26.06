import math
import sys

print('Для вывода справки о программе напишите в терминале: python mathtool.py --help')

if'--help' in sys.argv:
    print('''Справка: mathtool - решение уравнений вида ax^2+bx+c=0 Использование:
    python mathtool.py   
    вывод справки:
    python mathtool.py --help                
    ввод коэффициентов с клавиатуры
    python mathtool.py solve -a 1 -b -3 -c 2 решение с заданными коэффициентами

    Коэффициенты A, B, C — целые числа, по модулю не превышающие 10000''')
# Запрос у пользователя необходимых данных.Обработка недопустимого формата исходных данных
max_range=10000
try:
    a=int(input("Введите коэффицент а:"))
# Проверка на соответствие допустимому диапозону
    if abs(a) > max_range:
        print('Ошибка: значение вне допустимого диапозона; код возврата: 1', file=sys.stderr)
        sys.exit(1)
    b=int(input("Введите коэффицент b:"))
    if abs(b) > max_range:
        print('Ошибка: значение вне допустимого диапозона; код возврата: 1', file=sys.stderr)
        sys.exit(1)
    c=int(input("Введите коэффицент c:"))
    if abs(c) > max_range:
        print('Ошибка: значение вне допустимого диапозона; код возврата: 1' , file=sys.stderr)
        sys.exit(1)

# Определение вида уравнения
    if a==0:
#Линейное
        if b!=0:
            print(f'Уравнение линейное: x={-c/b:.3f}' )
#Не является уравнением
        if b==0:
            print('Не уравнение: неизвестного нет; код возврата 1' , file=sys.stderr)
            sys.exit(1)
#Квадратное
    else:
        D=b**2-4*a*c
        print(f'Квадратное; D={D};')
        if D>0:
            x1=(-b+math.sqrt(D))/(2*a)
            x2=(-b-math.sqrt(D))/(2*a)
            print(f'x1={x1:.3f}\nx2={x2:.3f}')
        elif D==0:
            x=-b/(2*a)
            print(f'x={x:.3f}')
        else:
            print('Действительных корней нет')

except ValueError:
    print('Ошибка: коэффицент не является целым числом; код возврата: 1', file=sys.stderr)
    sys.exit(1)




