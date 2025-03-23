# Purpose: Write sum of integers in list

numberList = [0,1,2,3,4,5,6,7,8,9,10]
def sumOfIntegersInList(numberList):
    sum = 0
    for i in numberList:
        sum = sum + i
    return sum

print("sum of integers in list:", sumOfIntegersInList(numberList))


    