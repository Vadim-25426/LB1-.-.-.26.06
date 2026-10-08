import math
MAX_TERMS = 10000
MAX_ITERATIONS = 100000
MIN_EPS = 0.0001

def znak(n):
    if n%2==0:
        return -1
    else:
        return 1

def term_sqplus(n):

    return znak(n) / (n * n + 1)

def term_third(n):
    return znak(n) / (3*n)

FORMULAS = {
    'sqplus': (term_sqplus,'S = 1/(1^2+1) - 1/(2^2+1) + 1/(3^2+1) - ...'),
    'third': (term_third,'S = 1/3 - 1/6 + 1/9 - 1/12 + ...')}
def sum_by_count(term_func, count):
    if count < 1 or count > MAX_TERMS:
        raise ValueError('количество слагаемых должно быть от 1 до 10000; код 1')
    res = 0.0
    for n in range(1, count + 1):
        res += term_func(n)
    return count, res

def sum_by_eps(term_func, eps):
    if not math.isfinite(eps) or eps <= 0 or eps < MIN_EPS:
        raise ValueError('точность должна быть больше 0 и не грубее 0.0001; код 1')
    res = 0.0
    n = 0
    while True:
        n += 1
        value = term_func(n)
        res += value
        if abs(value) < eps:
            return n, res
        if n >= MAX_ITERATIONS:
            raise ValueError('точность не достигнута; код 1')
        #ddsec