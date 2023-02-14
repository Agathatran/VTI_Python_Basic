class Student:
    def __init__(self,name_,age_,address_,mobile_number_):
        self.name = name_ #Muốn bên ngoài k truy cập được thì dùng __name
        self.age= age_
        self.address =address_
        self.mobile_number=mobile_number_

    def study(self,subject_name):
        print(f'I am studying {subject_name}')

    def watch_movie(self, movie_name):
        print(f'I am watching my favourite movie {movie_name}')

    def get_student(self): # Hàm này cũng có thể biến thành private bằng cách __get_student(self)
        print(f'Student information:')
        print(f'Name:{self.name}')
        print(f'Age:{self.age}')
        print(f'Address: {self.address}')
        print(f'Mobile Phone:{self.mobile_number}')

    def set_student(self,name_,age_,address_,mobile_number_):
        self.name=name_
        self.age=age_
        self.address = address_
        self.mobile_number = mobile_number_



'''std_1 = Student('Thanh', 50, 'KH', '45787')
std_1.get_student()
std_1.set_student('Linh',40,'HN','9358903')
std_1.get_student()

std_1.study('Titan')
std_1.watch_movie('Lala')'''

std_2=Student("Thanh Xau trai", 100, 'NT', '115000')
print(f'Name of student: {std_2.name}')
print(f'Age of student: {std_2.age}')
print(f'Address of student: {std_2.address}')
print(f'Mobile of student: {std_2.mobile_number}')
