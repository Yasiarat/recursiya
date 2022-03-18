def generate_numbers(n: int, m: int, prefix=None) -> None:
    """
    Выводит в консоль все перестановки длиной n в системе счисления n
    """
    if m > n:
        print('Оно так не работает, чувак')
        return

    if m == 0:
        print(*prefix)
        return
    prefix = prefix or []
    for digit in range(n):
        if digit not in prefix:
            prefix.append(digit)
            generate_numbers(n, m-1, prefix)
            prefix.pop()


generate_numbers(3, 3)
