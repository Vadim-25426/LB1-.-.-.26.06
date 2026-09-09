import math
import sys


try:
    a=int(input("Введите коэффицент а:"))
    b=int(input("Введите коэффицент b:"))
    c=int(input("Введите коэффицент c:"))
    if abs(a)>10000 or abs(b)>10000 or abs(c)>10000:
        print('Ошибка: значение вне допустимого диапозона' , file=sys.stderr)
        sys.exit(1)
    if a==0:
        if b!=0:
            print(f'Уравнение линейное: x={-c/b:.3f}' )
        if b==0:
            print('Не уравнение' , file=sys.stderr)
            sys.exit(1)

    else:
        D=b**2-4*a*c
        print(D)
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
    print('Ошибка: коэффицент не является целым числом', file=sys.stderr)
    sys.exit(1)




