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

stu_info = Student()
print(f'Name: {stu_info.name}')
print(f'Age: {stu_info.age}')
print(f'Email: {stu_info.email}')
print(f'Sex: {stu_info.sex}')


# 4.
# 4.1 Define a class named Geometry with 2 methods: get_area() and get_perimeter().
class Geometry():
    def __init__(self, length, width, radius):
        self.length=length
        self.width = width 
        self.radius = radius
    
# 4.2 Define a class named Square which inherited from Geometry class. This class has 2 attributes are length and width. 
# Override two methods from its parrent.

class Square(Geometry):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        area = self.length * self.width
        return area
    
    def get_perimether(self):
        perimether = 2* (self.length + self.width)
        return perimether
        
# 4.3 Define a class named Circle which inherited from Geometry class. This class has 1 attribute is radius. 
# Override 2 methods of its parrent  class.

class Circle(Geometry):
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        area = self.radius **2 *3.14
        return area
    
    def get_perimether(self):
        perimeter = self.radius *2 *3.14
    
def func(obj):
    obj.get_area()
    obj.get_perimether()

Circle_o= Circle()
Square_o = Square()

for shape in [Circle_o, Square_o]:
    func(shape)

# 4.4 Create a new object of class Square and a new object of class Circle. Print area and primeter of those.

