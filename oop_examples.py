''' #1. Create a new class with some properties and methods
import datetime
class Vehicle:
    def __init__(self,name, max_speed = 100, color = 'red' , year = 2020) -> None:
        self.name = name #public property
        self._max_speed = max_speed # protected property with single underscore
        self.__color = color #private property with double underscore
        self.__year = year

    def get_name(self):
        return self.name 
    
    def get_max_speed(self):
        return self._max_speed 
    
    def get_color(self):
        return self.__color 
    
    def __cal_year_old(self):
        year_old = datetime.datetime.now().year - self.__year
        return year_old
    
    def get_year_old(self):
        return self.__cal_year_old()
    
    def get_color(self, color):
        self.__color = color 

    def get_max_speed(self):
        self._max_speed = max_speed
    
    #2. Create a Child class
class Motor(Vehicle):
    def __init__(self, name, color, max_speed, year, engine) -> None:
        self.engine = engine
        super().__init__(name, max_speed, color, year)
    
    def get_engine(self):
        return self.__engine
    
    def get_max_speed(self):
        return self._max_speed + 50


# Define a new object of child class
motor_o = Motor('Air Blade', 'black', 200, 2017, 150)
print('------------------- Motor Information-------------')
print(f'Name:{motor_o.get_name()}')
print(f'Color: {motor_o.get_color}')
print(f'Max_speed: {motor_o.get_max_speed()}')
print(f'Year Old: {motor_o.get_year_old}')
'''
#
'''
3. Define class Car which inherited from Vehicle.
- Add 1 more property: Branch
- Add 1 more method to return branch information
- Overide method get_year_old(): add more year old for each Car
-Init a Car object, then print all information

class Car(Vehicle):
    def __init__(self, name, branch, color, max_speed, year, engine):
        self.branch = branch
        super().__init__(name, color, max_speed, year, engine)

    def get_branch(self):
        return self.branch
    
    def add_year_old(self):
        return self.year_old +1

New_car = Car('Sonata', 'Hyundai', 'black', 300, 2017, 150)
print('------------------- Car Information-------------')
print(f'Name:{New_car.get_name()}')
print(f'Branch: {New_car.get_branch()}')
print(f'Color: {New_car.get_color}')
print(f'Max_speed: {New_car.get_max_speed()}')
print(f'Year Old: {New_car.get_year_old}')

veh_o= Vehicle('Bicycle', 10, 'Green', year = 2018)
print(f'Max speed: {veh_o._max_speed}')

class Bird:
    def __init__(self):
        pass

    def intro(self):
        print("There are many types of birds here")

    def flight(self):
        print("Most of the bird can fly on the sky, so others cannot")

class Eagle(Bird):
    def __init__(self):
        super().__init__()

    def flight(self):
        print('Eagle can fly')

class Ostrict(Bird):
    def __init__(self):
        super().__init__()

    def flight(self):
        print('Ostrict cannot fly')

bird_o= Bird()
Eagle_o = Eagle()
Ostrict_o = Ostrict()

bird_o.intro()
bird_o.flight()
Eagle_o.intro()
Eagle_o.flight()
Ostrict_o.intro()
Ostrict_o.flight()     
'''
from abc import ABC, abstractmethod

class Polygon:
    @abstractmethod
    def no_of_sides(self):
        pass 

class Triangle(Polygon):
    #override abstract method from parent class
    def no_of_sides(self):
        print('The triangle has 3 sides')

class Hexagon(Polygon):
    def no_of_sides(self):
        print('The hexagon has 6 sides')

trg_o= Triangle()
trg_o.no_of_sides()

hxg_o = Hexagon()
hxg_o.no_of_sides()