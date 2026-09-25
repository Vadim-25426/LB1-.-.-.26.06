import math

MAX_VALUE = 10000


def check_coefficients(coefficients: dict[str, int]):
    #Проверка коэффициентов на допустимый диапазон
    for name, value in coefficients.items():
        if abs(value) > MAX_VALUE:
            raise ValueError(f"коэффициент {name} вне допустимого диапазона")


def solve(a: int, b: int, c: int):

    if a == 0:
        if b == 0:
            # Не уравнение
            return "не уравнение", None, []
        # Линейное
        x = -c / b
        return "линейное", None, [x]

    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return "квадратное", D, [x1, x2]
    elif D == 0:
        x = -b / (2 * a)
        return "квадратное", D, [x]
    else:
        return "квадратное", D, []
