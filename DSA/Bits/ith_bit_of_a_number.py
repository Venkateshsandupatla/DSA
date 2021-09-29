n = 17    # its binary is 10001

def ith(i):
    a = 1<<(i-1)
    print((n&a) >> (i-1))

ith(3)