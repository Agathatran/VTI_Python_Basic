# 1. Define a class named Student and initialize attributes: name, age, email and sex. Create a new object of that class.
class Student():
    def __init__(self, name, age, email, sex):
        self.name = name
        self.age = age
        self.email = email
        self.sex = sex
# 2. Define a class named People with no attributes and mothods. Create a new object of that class.
class People():
    def __init__(self):
        pass
# 3. 
# 3.1 Define a class named Staff with attributes: role, department, salary and a method named show_details() to display all attributes.
# department attribute is protected, salary attribute is private.
class Staff():
    def __init__(self, role, department, salary,):
        self.role = role
        self._department = department
        self.__salary = salary

    def show_detail(self):
        print(f'Role: {self.role}')
        print(f'Department: {self._department}')
        print(f'Salary: {self.__salary}')

# 3.2 Define a class named Student with inherited from Staff class. This class has more 2 attributes: name and age.

class Student(Staff):
    def __init(self, role, department, salary, name, age):
        self.name = name
        self.age = age
        super().__init__(role, department, salary)

# 3.3 Create a new object of Student then show all attributes of that object.
# ---> DON'T UNDERSTAND
# 4.
# 4.1 Define a class named Geometry with 2 methods: get_area() and get_perimeter().
class Geometry():
    def __init__(self, length, width, radius):
        self.length=length
        self.width = width 
        self.radius = radius

    def get_area(self):
        area = self.length * self.width
        return area
    
    def get_perimether(self):
        perimether = 2* (self.length + self.width)
        return perimether
    
# 4.2 Define a class named Square which inherited from Geometry class. This class has 2 attributes are length and width. 
# Override two methods from its parrent.

class Square(Geometry):
    def __init__(self, length, width):
        super().__init__(length, width)
# 4.3 Define a class named Circle which inherited from Geometry class. This class has 1 attribute is radius. 
# Override 2 methods of its parrent  class.

# 4.4 Create a new object of class Square and a new object of class Circle. Print area and primeter of those.

