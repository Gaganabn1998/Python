 #Write one Method overloading  program

class MethodOverloading:
    def add(self, a, b=None, c=None):
        if b is not None and c is not None:
            return a + b + c
        elif b is not None:
            return a + b
        else:
            return a


# Create an object of the class
obj = MethodOverloading()

 
print("Addition of two numbers:", obj.add(2, 3))     
print("Addition of three numbers:", obj.add(2, 3, 4)) 
print("Addition of one number:", obj.add(5))         


