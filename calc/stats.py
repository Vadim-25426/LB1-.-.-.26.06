import sys
import math
MAX_VALUE = 10_000

def schet_nums(arr):

    numbers = []
    for line in arr:
        for word in line.split():
            try:
                numbers.append(float(word))
            except ValueError:
                raise ValueError(f"{word} не является числом")
    if len(numbers) == 0:
        raise ValueError("Список пуст")
    if len(numbers) > 20:
        raise ValueError("Кол-во элементов в списке > 20")
    if any((not math.isfinite(word)) for word in numbers):
        raise ValueError("Числа должны быть конечными")
    if any(abs(word) > MAX_VALUE for word in numbers):
        raise ValueError(f"Числа должны быть по модулю не должны превышать 10000")
    return numbers