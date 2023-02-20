#1. Create a new class with some properties and methods
import datetime
class Vehicle:
    def __init__(self, name, max_speed =100, color = 'red', year = 2020):
        self.name = name
        self._max_speed = max_speed
        self.__color = color
        self.__year = year 

    def get_name(self):
        return self.name 
    
    def get_max_speed(self):
        return self._max_speed
    
    def get_color(self):
        return self.__color 
    
    def __cal_yearold(self):
        year_old = datetime.datetime.now().year - self.__year
        return year_old
    
    def get_yearold(self):
        return self.__cal_yearold()
    
    def set_color(self,color):
        self.__color = color 

    def set_max_speed(self, max_speed):
        self._max_speed = max_speed

# 2. Create a Child class

class Motor(Vehicle):
    def __init__(self, name, engine, max_speed=100, color='red', year = 2020) -> None:
        self.engine=engine
        super().__init__(name,max_speed, color, year)

#Define a new object of child class

motor_o = Motor("Aire blade", 150, max_speed = 200, color='Black', year = 2009)
print('------Motor\'s info------')
print(f'Name : {motor_o.get_name()}')
print(f'Color: {motor_o.get_color()}')
print(f'Max speed: {motor_o.get_max_speed()}')
print(f'Year: {motor_o.get_yearold()}')


