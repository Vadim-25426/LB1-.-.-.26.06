import argparse

def build_razb():
    parser = argparse.ArgumentParser(prog='mathtool',allow_abbrev=False,description='Инструмент для математических вычислений')
    subparsers = parser.add_subparsers(dest='command', help='Доступные команды')

    #solve
    sol_p = subparsers.add_parser('solve', allow_abbrev=False, help='Решение уравнения')
    sol_p.add_argument('-a', type=int, help='Коэффициент A')
    sol_p.add_argument('-b', type=int, help='Коэффициент B')
    sol_p.add_argument('-c', type=int, help='Коэффициент C')

    #stats
    stats_p = subparsers.add_parser('stats', allow_abbrev=False, help='Показатели последовательности')
    stats_p.add_argument('--input', type=str, help='Файл с числами')

    #series
    ser = subparsers.add_parser('series', allow_abbrev=False, help='Сумма ряда')
    ser.add_argument('--func', required=True, help='Ряд: third, sqplus')
    gr = ser.add_mutually_exclusive_group(required=True)
    gr.add_argument('--terms', type=int, help='Количество слагаемых')
    gr.add_argument('--eps', type=float, help='Точность')

    #integrate
    int_p = subparsers.add_parser('integrate', allow_abbrev=False, help='Численное интегрирование')
    int_p.add_argument('--func', required=True, help='Функция: ratio, root')
    int_p.add_argument('--from', dest='start', type=float, required=True, help='Нижний предел')
    int_p.add_argument('--to', type=float, required=True, help='Верхний предел')
    int_p.add_argument('--steps', type=int, required=True, help='Количество шагов')

    return parser





