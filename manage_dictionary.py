#Write program to Add, Delete, Discard and Update value in dictionary 

def mangeDictionary():
    dict = {}
    dict["name"] = "John"
    dict["age"] = 25
    print("Initial Dictionary:", dict)

    #Update value in dictionary
    dict.update(age = 26)
    print("Updated Dictionary:", dict)

    #Add value in dictionary
    dict["Favorite Color"] = "Blue"
    print("Dictionary after adding value:", dict)

    #Delete value in dictionary
    del dict["Favorite Color"]
    print("Dictionary after deleting value:", dict)

    #Discard value in dictionary
    dict.pop("age") 
    print("Dictionary after discarding value:", dict)


mangeDictionary()
