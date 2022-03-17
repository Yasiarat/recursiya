def gcd(a: int, b: int) -> int:
    """
    возвращает НОД от числа а и b, вычесленный по алгоритму Евклида
    """
    #условие-призрак: b != 0

    return gcd(b, a % b) if b else a

print(gcd(4, 5))