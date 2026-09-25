MAX_VALUE = 10_000



def read_numbers(lines): #Разбор строк в список чисел. lines — список строк или файловый объект.
    numbers = []
    for line in lines:
        for word in line.split():
            try:
                numbers.append(float(word))
            except ValueError:
                raise ValueError(f"'{word}' не является числом")
    if len(numbers) == 0:
        raise ValueError("Список пуст")
    if len(numbers) > 20:
        raise ValueError("Количество чисел превышает 20")
    if any(not math.isfinite(n) for n in numbers):
        raise ValueError("Числа должны быть конечными")
    if any(abs(n) > MAX_VALUE for n in numbers):
        raise ValueError("Числа по модулю не должны превышать 10000")
    return numbers


def lenn(nums):
    return len(nums)

def summa(nums):
    return sum(nums)

def sr_arif(nums):
    return sum(nums) / len(nums)

def sum_kv(nums):
    return sum(x ** 2 for x in nums)

def sr_kv(nums):
    return math.sqrt(sum_kv(nums) / len(nums))

def dispercy(nums):
    avg = sr_arif(nums)
    return sum((x - avg) ** 2 for x in nums) / len(nums)

def sko(nums):
    #СКО — корень из дисперсии
    return math.sqrt(dispercy(nums))

def stand_otkl(nums):
    if len(nums) < 2:
        return None
    avg = sr_arif(nums)
    return math.sqrt(sum((x - avg) ** 2 for x in nums) / (len(nums) - 1))

def minimum(nums):
    return min(nums)

def maximum(nums):
    return max(nums)

def positive_count(nums):
    return len([x for x in nums if x > 0])

def negative_count(nums):
    return len([x for x in nums if x < 0])


# Таблица показателей(метка, функция, формат)
reports = [
    ("Количество",       lenn,             "d"),
    ("Сумма",            summa,            ".3f"),
    ("Сред. арифм.",     sr_arif,             ".3f"),
    ("Сумма кв.",        sum_kv,   ".3f"),
    ("Ср. кв.",          sr_kv, ".3f"),
    ("Дисперсия",        dispercy,         ".3f"),
    ("СКО",              sko,      ".3f"),
    ("Станд. откл.",     stand_otkl,   ".3f"),
    ("Наименьшее",       minimum,          ".3f"),
    ("Наибольшее",       maximum,          ".3f"),
    ("Положительных",    positive_count,    "d"),
    ("Отрицательных",    negative_count,    "d"),
]


def compute(nums):
    #Вычисляет все показатели. Возвращает список (label, value)
    results = []
    for label, func, form in reports:
        value = func(nums)
        if value is None:
            raise ValueError(f'{label} не существует')
        results.append((label,f'{value:{form}}'))
    return results
