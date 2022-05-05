def n1():
    x = '7'* 1000 + '3' * 1000
    while '777' in x or '333' in x:
        x = x.replace('777', '3', 1)
        x = x.replace('333', '7', 1)

    print(x)


def n2():
    print('x', 'y', 'z', 'w')
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    F = (x <= y) and (y <= w) and (z <= x)
                    if F:
                        print(x, y, z, w)


def n3(s = 216):
    n = 400
    while s > 0:
        s //= 6
        n -= 25
    print(n)


def n4():
    for i in range(1, 1000):
        n = i
        bin_n = bin(n)[2:]
        bin_n += bin_n[-1] * 2
        if bin_n.count('1') % 2 == 0:
            bin_n += '0'
        else:
            bin_n += '1'
        r = int(bin_n, 2)
        if n > 84:
            print(i)
            break



def n():
    x = 49 ** 28 + 7 ** 20 - 343**8
    x_str = ''
    while x:
        x_str += str(x % 7)
        x //= 7
    print(x_str.count('1'))


def n0():
    t = [0, 0, 1, 1, 1]
    for i in range(5, 11):
        t.append(t[i - 1] + (t[i // 4] if not i % 4 else 0))
    print(t)
    for i in range(11, 81):
        if i == 30:
            t.append(0)
        elif i >= 40:
            t.append(t[i - 1] + (t[i // 4] if not i % 4 else 0))
        else:
            t.append(t[i - 1])
    print(t)


def n0r(n):
    if n < 2 or n == 30:
        return 0
    elif n < 4:
        return 1
    else:
        if n % 4 == 0:
            return n0r(n - 1)
        else:
            return n0r(n - 1)


def dell():
    for A in range(1, 1000):
        flag = True
        for x in range(1, 10000):
            if ( (x % 25 != 0 or x % 60 != 0) <= (x % A != 0)) == 0:
                flag = False
                break
        if flag:
            print(A)
            break


dell()
