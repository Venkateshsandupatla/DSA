n = 5 #101
def reset(k):
    a = ~(1<<(k-1))
    #print(a)
    print(n&a)

reset(1)

#https://www.geeksforgeeks.org/program-to-clear-k-th-bit-of-a-number-n/