
#Write program to find the sum of all items in a dictionary,Set, Tuple ,List                    

def sumOfAllItemsInSetTuppleList():
    #Sum of all items in dictionary
    mydict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
    print("Sum of all items in dictionary:", sum(mydict.values()))
    
    #Sum of all items in set
    myset = {10, 20, 30, 40, 50}
    print("Sum of all items in set:", sum(myset))
    
    #Sum of all items in tuple
    mytuple = (10, 20, 30, 40, 50)
    print("Sum of all items in tuple:", sum(mytuple))
    
    #Sum of all items in list
    mylist = [10, 20, 30, 40, 50]
    print("Sum of all items in list:", sum(mylist))

sumOfAllItemsInSetTuppleList()