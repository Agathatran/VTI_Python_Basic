#mymodule.py
def circle():
    r=float(input("Input the radius: "))
    perimeter=math.py*r*2
    area=math.py*r**2
    print(f'The perimater is: {perimeter}')
    print(f'The area is: {area}')

import mymodule
mymodule.circle(4)