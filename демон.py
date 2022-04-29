def n1():
    x = 49 ** 28 + 7 ** 20 - 343**8
    x_str = ''
    while x:
        x_str += str(x % 7)
        x //= 7
    print(x_str.count('1'))


def n2():
    #t = [0, 0, 1, 1, 1]
    t = [0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2]
    for i in range(11, 81):
        if i != 30:
            t.append(t[i - 1] + (t[i // 4] if not i % 4 else 0))
    print(t)



def n2r(n):
    if n < 2 or n == 30:
        return 0
    elif n < 4>:
        return 1
    else:
        if n % 4 == 0:
            return n2r(n - 1)
        else:
            return n2r(n - 1)

n2()