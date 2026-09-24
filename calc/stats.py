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

def summa(nums) :
    res = 0
    for num in nums:
        res += num
    return res

def sr_arif(nums) :
    return sum(nums) / len(nums)

def minimum(nums: list[float]) -> float:
    res = 0
    for num in nums:
        if num < res:
            res = nums
    return res

def positive_count(nums):
    return len([x for x in nums if x > 0])

def negative_count(nums):
    return len([x for x in nums if x < 0])

def sum_kv_otkl(nums: list[float]) -> float:
    sr_znach = sr_arif(nums)
    res = 0
    for num in nums:
        res += (num - sr_znach) ** 2
    return res

def dispercy(nums: list[float]) -> float:
    return sum_kv_otkl(nums) / len(nums)

def stand_otkl(nums: list[float]) -> float | str:
    if len(nums) < 2:
        return "значения нет"
    return math.sqrt(sum_kv_otkl(nums) / (len(nums) - 1))
