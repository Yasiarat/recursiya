def power(a: float, n: int) -> float:
    """
    Возводит число а в натуральную степень n
    """
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(a*a, n // 2)
    # условие-призрак: n % 2 != 0
    return power(a, n - 1) * a


print(power(2, 1))
