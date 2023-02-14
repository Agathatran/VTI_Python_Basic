'''
Tạo class Vehicle:
- có 2 thuộc tính là max_speed và name. Hai thuộc tính được gán giá trị khởi tạo lúc khai báo đối tượng của class
- Hai phương thức:
+phương thức get_veh(): Hiển thị thông tin về các thuộc tính của đối tượng class
+ phương thức set_veh: Gán giá trị mới cho các thuộc tính của đối tượng
+ phương thức check_speed(): kiểm tra tốc độ của đối tượng theo các giá trị: 0-30: slow, 30-70: Normal, >70: Fast. In ra thông báo tương ứng

2. Tạo hai đối tượng của class
3. Hiển thị thông tin của các đối tượng vừa tạo
4. Cập nhật thông tin mới cho một trong 2 đối tượng. Kiểm tra lại hành động cập nhật bằng cách hiển thị thông tin mới
5. Hiển thị thông tin về dải tốc độ của 2 đối tượng
6. Biến tất cả các thuộc tính và phương thức của class (trừ phương thức get_veh() và set_veh() thành private rồi thực hiện lại yêu cầu từ số 3 đến số 5. Xem kết quả và giải thích)
'''

class Vehicle:
    def __init__(self, max_speed, name):
        self.__max_speed = max_speed
        self.__name = name

    def get_veh(self):
        print(f'Max speed: {self.__max_speed}')
        print(f'Name: {self.__name}')

    def set_veh(self,max_speed_, name_):
        self.__max_speed=max_speed_
        self.__name=name_
    
    def check_speed(self):
        if ((self.__max_speed>=0) and (self.__max_speed<30)):
            print("Slow")
        elif ((self.__max_speed >=30) and (self.__max_speed <70)):
            print("Normal")
        else:
            print("Fast")
Veh1= Vehicle(100,'Minicooper')
Veh2 = Vehicle(20,'Sonata')
print('------Veh1\'s info------')
Veh1.get_veh()
print('------Veh2 \'s info------')
Veh2.get_veh()
print('------Update to Veh1-------')
Veh1.set_veh(30,'Avante')
Veh1.get_veh()
print('____________')
Veh1.check_speed()
Veh2.check_speed()