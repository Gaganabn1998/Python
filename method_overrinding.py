 #Write one Method overridding  program
class Parent:
    def show(self):
    
        print("Sum Inside Parent Class", 2+3)            
class Child(Parent):
    def show(self):
        super().show()
        print("Sum Inside Parent Class", 4+5)    
obj = Child()
obj.show()  # Output: Inside Child Class

