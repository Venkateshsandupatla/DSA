n = int(input("Enter a number: "))

def odd_even(number):
    if number & 1 == 1:
        print("the given number is odd ")
    else:
        print("Its even number")

odd_even(n)