def n10():
    str_number = ''
    number = 16 ** 23 + 4 ** 12 - 32 ** 6
    while number > 0:
        ost = number % 4
        str_number += str(ost)
        number //= 4
    print(str_number[::-1])
    for i in range(4):
        print(str_number.count(str(i)))




def n2():
    print('x', 'y', 'z', 'w')
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if((x <= y) and ((not x) <= (not z)) or w) == 0:
                        print(x, y, z, w)


n2()