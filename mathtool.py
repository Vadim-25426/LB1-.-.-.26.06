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
    sys.exit(0)
# Запрос у пользователя необходимых данных.Обработка недопустимого формата исходных данных
max_range=10000
a=0
b=0
c=0
if len(sys.argv)==8:
    if sys.argv[2]=='-a' and sys.argv[4]=='-b' and sys.argv[6]=='-c':
        try:
            a=int(sys.argv[3])
            b=int(sys.argv[5])
            c=int(sys.argv[7])
            if abs(a)>max_range or b>max_range or c >max_range:
                print('Ошибка: значение вне допустимого диапозона; код возврата: 1', file=sys.stderr)
                sys.exit(1)
        except ValueError:
            print('Ошибка: коэффицент не является целым числом; код возврата: 1', file=sys.stderr)
            sys.exit(1)
elif 2<len(sys.argv)<8:
    print('Вы не ввели коэффицент(ы); код возврата 1', file=sys.stderr)
    sys.exit(1)
else:
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
    except ValueError:
        print('Ошибка: коэффицент не является целым числом; код возврата: 1', file=sys.stderr)
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