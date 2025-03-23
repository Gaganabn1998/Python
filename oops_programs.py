# Parent Class
class Employee:
    # Constructor to initialize Employee attributes
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    # Method to display employee details
    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)


# Child Class: Developer
class Developer(Employee):
    def __init__(self, name, age, salary, language):
        # Call the parent class constructor using super()
        super().__init__(name, age, salary)
        self.language = language

    # Override the show() method to display language
    def show(self):
        super().show() 
        print("Programming Language:", self.language)


# Child Class: Manager
class Manager(Employee):
    def __init__(self, name, age, salary, team):
        # Call the parent class constructor using super()
        super().__init__(name, age, salary)
        self.team = team

    # Override the show() method to display team
    def show(self):
        super().show()  
        print("Team:", self.team)


# Create a Developer object
dev = Developer("John", 25, 50000, "Python")
print("Developer Details:")
dev.show()

print("\n")

# Create a Manager object
manager = Manager("David", 30, 70000, "Development")
print("Manager Details:")
manager.show()





