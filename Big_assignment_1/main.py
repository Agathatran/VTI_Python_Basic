from student import Student
from subject import subject
from score import Score
import time

def main_flow():
    print('************ Chao mung ban den voi he thong quan ly sinh vien va mon hoc ****************')
    print('**********************Vui long chon mot chuc nang ben duoi.*******************************')
    print("1. Quan ly sinh vien")
    print('2. Quan ly mon hoc')
    print('3. Quan ly diem so')
    print('4. Thoat chuong trinh')
    # Nhan thong tin tu ban phim
    while True:
        user_input = input("Chon chuc nang: ")
        if user_input == '1':
            stu_obj = Student()
            stu_obj.display_menu()
        elif user_input == '2':
            sub_obj = subject()
            sub_obj.display_menu()
        elif user_input == '3':
            score = Score()
            score.display_menu()
        elif user_input == '4':
            print("BYE BYE")
            time.sleep(1)
            return #hoac exit
        else:
            print('Vui long nhap dung ma so chuc nang quy dinh')


if __name__ == '__main__':
    main_flow()