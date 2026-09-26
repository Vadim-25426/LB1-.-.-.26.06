import sys
from calc.equation import *
from cli import build_razb
from calc.stats import *


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
def start_solve(args):
    #Команда solve — решение уравнения
    # Если параметры не заданы — читаем с клавиатуры
    if args.a is None or args.b is None or args.c is None:
        if args.a is not None or args.b is not None or args.c is not None:
            raise ValueError("укажите либо все три коэффициента, либо ни одного")
        a = int(input("A = "))
        b = int(input("B = "))
        c = int(input("C = "))
    else:
        a, b, c = args.a, args.b, args.c

    check_coefficients({"A": a, "B": b, "C": c})
    kind, D, roots = solve(a, b, c)

    if kind == 'не уравнение':
        print('Не уравнение')
    elif kind == "линейное":
        print('Уравнение линейное')
        print(f'x = {roots[0]:.3f}')
    else:
        print('Уравнение квадратное')
        print(f'Дискриминант: {D}')
        if len(roots) == 2:
            print(f'x1 = {roots[0]:.3f}')
            print(f'x2 = {roots[1]:.3f}')
        elif len(roots) == 1:
            print(f'x = {roots[0]:.3f}')
        else:
            print('Действительных корней нет')

    return 0
def main(argv):
    parser = build_razb()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0
    commands={
        'solve': start_solve}

    try:
        return commands[args.command](args)

    except (ValueError, OSError) as e:
        print(f'Ошибка: {e}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))