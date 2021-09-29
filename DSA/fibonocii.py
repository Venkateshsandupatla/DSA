n = int(input())
def fisum(n):
    a = 0
    b = 1
    sum = 1
    if n == 0 :
        print(0)
    elif n == 1:
        print(0)
    elif n == 2:
        print(1)
    else:
        for i in range(2,n):
            c = a + b
            sum = sum+c
            a = b
            b = c
        print(sum)
    
    
       
fisum(n)