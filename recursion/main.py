# How to find the sum of digits of a positive integer number using recursion ?

def sumOfDigit(n):
    assert n >= 0 , "Given digit must be positive or greater than zero"
    if n == 0:
        return 0
    print("n % 10 : ",n%10)
    print("n/10 : ",n/10)
    div = (int) (n/10)
    rem = (int) (n % 10)
    return rem + sumOfDigit(div)
print(sumOfDigit(1234))
