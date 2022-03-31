def fib(n: int) -> int:
    '''
    Возвращает n-ное число Фибоначи. Реализуется с помощью рекурсии
    '''
    if n <= 1:
        return n
    if n <= 2:
        return 1
    return fib(n - 2) + fib(n - 1)


def fib2(n: int) -> int:
    '''
    Возвращает n-ное число Фибоначи. Реализуется с помощью рекурсии. Запоминает.
    '''
    if n >= len(fib_list):
        a = fib2(n - 1) + fib2(n - 2)
        fib_list.append(a)
    return fib_list[n]


def fib3(n):
    fibanachy = [0, 1]
    for i in range(2, n + 1):
        fibanachy.append(fibanachy[i - 1] + fibanachy[i - 2])
    return fibanachy[n]


fib_list = [0, 1]

print(fib3(100))
print(fib2(100))
print(fib(100))

