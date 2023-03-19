from objects.student import Student
from objects.subject import Subject
from objects.score import Score
import time

def main_flow():
   
    while True:
        # hien thi danh sach chuc nang
        print('-----------------------------------------------------------------')
        print('******* CHAO MUNG BAN DEN VOI HE THONG QUAN LY SINH VIEN ********')
        print('************ Vui long chon mot chuc nang ben duoi ***************')
        print('1. Quan ly sinh vien')
        print('2. Quan ly mon hoc')
        print('3. Quan ly diem so')
        print('4. Thoat chuong trinh')

        # nhan thong tin tu ban phim
        user_input = input('Chon chuc nang: ')
        if user_input == '1':
            st_obj = Student()
            st_obj.display_menu()
        elif user_input == '2':
            sub_obj = Subject()
            sub_obj.display_menu()
        elif user_input == '3':
            score = Score()
            score.display_menu()
        elif user_input == '4':
            print('BYE BYE')
            time.sleep(1)
            return
        else:
            print('Vui long nhap dung ma so chuc nang quy dinh')
        
if __name__ == '__main__':
    main_flow()