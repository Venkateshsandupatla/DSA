# in given array every number appears twice except one number we have to find that number

# this is the brutt method it takes O(n2)
def bu(array):
    b = []
    for i in range(0,len(array)):
        a = array[i]
        
        count1 = 1
        for j in range(i+1, len(array)):
            
            if array[j] == a:
                count1+=1
                b.append(arr[j])
                break
        if count1 != 2 and a not in b:
            print("Its the number {}".format(a))
 #   print(len(b))

a = [1,3,4,1,2,3,4,2,6]
bu(arr)

#DSA by kunal youtube
# this is optimized way 
# here we use XOR operator we know that a^a == 0
# so if we do 1^3^4^1^2^3^4^2^6  two 1's,2's,3's,4's will become zero 
# remaining will be 6 we will print it 
def XOR(arra):
    unique =arra[0]
    for i in range(1,len(arra)):
        unique^=arra[i]   #  1^3^4^1^2^3^4^2^6
    print(unique)        
XOR(a)