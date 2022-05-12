def domaetodoma():
    for x in range(1000):
        r = 216 ** 5 + 6 ** 3 - 1 - x
        s = ''
        while r:
            s += str(r % 6)
            r //= 6
        if s.count('5') == 12:
            print(x)
            break


domaetodoma()
