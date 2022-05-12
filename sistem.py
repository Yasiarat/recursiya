def domaetodoma():
    for x in range(10):
        r = 216 ** 5 + 6 ** 3 - 1 - x
        s = ''
        while x:
            s += str(x % 2)
            x //= 2
        print(s.count('1'))


domaetodoma()