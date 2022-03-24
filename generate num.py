def generate_numbers(n: int, m: int, prefix=None) -> None:
    """
    Выводит в консоль все перестановки длиной n в системе счисления n
    """
    if m > n:
        raise ValueError('Оно так не работает, чувак') # выдаём ошибку

    if m == 0:
        print(*prefix)
        return
    prefix = prefix or []
    for digit in range(n):
        if digit in prefix:
            continue
        prefix.append(digit)
        generate_numbers(n, m-1, prefix)
        prefix.pop()


generate_numbers(1, 5)
