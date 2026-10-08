import sys
from calc.equation import *
from cli import build_razb
from calc.stats import *
from calc.series import *
from calc.integrate import *


def start_solve(args):
    #Команда solve — решение уравнения
    # Если параметры не заданы — читаем с клавиатуры
    if args.a is None or args.b is None or args.c is None:
        if args.a is not None or args.b is not None or args.c is not None:
            raise ValueError("укажите либо все три коэффициента, либо ни одного; код 1")
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
def start_stats(args):
    if args.input:
        with open(args.input, encoding='utf-8') as source:
            nums = read_numbers(source)
    else:
        nums = read_numbers(sys.stdin)

    results =compute(nums)

    for label, value, form in results:
        if value is None:
            print(f"{label}: НЕ СУЩЕСТВУЕТ; код 1")
        else:
            print(f"{label}: {value:{form}}; код 1")

    return 0
def start_series(args):
    if args.func not in FORMULAS:
        raise ValueError(f'неизвестный ряд: {args.func}')

    term_func, description = FORMULAS[args.func]  # Достаём функцию-слагаемое (term_third или term_sqplus)

    if args.terms is None and args.eps is None:
        raise ValueError('Необходимо указать либо --terms, либо --eps')
    elif args.terms is None:
        count, total = sum_by_eps(term_func, args.eps)
    elif args.eps is None:
        count, total = sum_by_count(term_func, args.terms)
    else:
        raise ValueError('Нельзя указывать одновременно --terms и --eps')
    print(FORMULAS[args.func])
    print(f"Слагаемых: {count}")
    print(f"Сумма ряда: {total:.4f}")
    return 0
def start_integrate(args):
    if args.func not in FUNCTIONS:
        raise ValueError(f'неизвестный ряд: {args.func}; код 1')
    return integral(args.func, args.start, args.to, args.steps)


def main(argv):
    parser = build_razb()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0
    commands={
        'solve': start_solve,
        'stats': start_stats,
        'series': start_series,
        'integrate': start_integrate}

    try:
        return commands[args.command](args)

    except (ValueError, OSError) as e:
        print(f'Ошибка: {e}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))