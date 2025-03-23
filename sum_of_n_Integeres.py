# Purpose: To calculate the sum of first n integer numbers
n = 10
def sumOfnIntegers(n):
    sum = 0 
    for i in range(0, n+1):
        sum = sum + i   
    return sum  
print("sum of first",n,"numbers",sumOfnIntegers(n))
