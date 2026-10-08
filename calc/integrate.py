import math
def prov(a, b, steps):
    if not (math.isfinite(a) and math.isfinite(b)):
        raise ValueError('Границы интегрирования должны быть конечными числами; код 1')
    if b <= a:
        raise ValueError('Начальный предел не меньше конечного; код 1')
    if not (1 <= steps <= 100000):
        raise ValueError('Количество шагов должно быть в диапазоне [1, 100000]; код 1')


def F_ratio(x):
    return x / (x+1)

def F_root(x):
    return math.sqrt(x**2+1)

FUNCTIONS={
    'ratio':(F_ratio, 'F(x) = x / (x+1)', 0, 20, '.4f'),
    'root':(F_root, 'F(x) = sqrt(x^2 + 1)', -5, 5, '.4f'),
}

def integral(f_name, a, b, steps):
    if f_name not in FUNCTIONS:
        raise ValueError('Неизвестная функция; код 1')
    F, formula, low, high, form = FUNCTIONS[f_name]
    if f_name == 'ratio':
        if low>a and high<b:
            raise ValueError('предел вне промежутка этой функции; код 1')
    if f_name == 'root':
        if low>=a and high<=b:
            raise ValueError('предел вне промежутка этой функции; код 1')
    prov(a, b, steps)
    dx = (b - a) / steps
    res=0
    for i in range(steps):
        x = a + i * dx
        res += F(x) * dx
    return f'Значение интеграла:{res:{form}}'