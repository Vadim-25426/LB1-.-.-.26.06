import math

def solve(a,b,c):
    if a<=10000 and b<=10000 and c<=10000:
        try:
            if a == 0:
                # Линейное
                if b != 0:
                    return f'Уравнение линейное: x={-c / b:.3f}'
                # Не является уравнением
                else:
                    return 'Не уравнение: неизвестного нет; код возврата 1'
            # Квадратное
            else:
                D = b ** 2 - 4 * a * c
                if D > 0:
                    x1 = (-b + math.sqrt(D)) / (2 * a)
                    x2 = (-b - math.sqrt(D)) / (2 * a)
                    return f'Квадратное; D={D}; x1={x1:.3f}\nx2={x2:.3f}'
                elif D == 0:
                    x = -b / (2 * a)
                    return f'Квадратное; D={D}; x={x:.3f}'
                else:
                    return 'Действительных корней нет'
        except ValueError:
            raise ValueError('Ошибка: коэффицент не является целым числом; код возврата: 1')
    else:
        return 'Число по модулю превышает 10000'
d=solve(0, 1000 ,3)
print(d)