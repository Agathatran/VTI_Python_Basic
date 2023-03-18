
from utlis import *
import time
from database_connection import *
class Student:
    def __init__(self, st_ID = '', st_name = '', st_dob = '', st_sex = '',st_address = '', st_mobile = '', st_email = ' ') -> None:
        self.st_ID = st_ID
        self.st_name = st_name 
        self.st_dob = st_dob 
        self.st_sex = st_sex
        self.st_address = st_address
        self.st_email = st_email
        self.st_mobile = st_mobile

    def display_menu(self):
        while True:
            print('----------------------------------------------------------------')
            print("Chon mot trong cac chuc nang ben duoi:")
            print("1. Them moi sinh vien")
            print("2. Cap nhat thong tin sinh vien")
            print("3. Xoa thong tin sinh vien")
            print("4. Tim kiem thong tin sinh vien")
            print("Bam 5 de quay lai menu truoc do")
            user_input = input("Chon chuc nang")
            if user_input == "1":
                self.add_student()
            elif user_input == "2":
                self.update_student()
            elif user_input == "3":
                self.delete_student()
            elif user_input =="4":
                self.search_student()
            elif user_input == "5":
                print("BYE BYE!")
                time.sleep(1)
                return
            else:
                print("Vui long nhap dung ma so chuc nang!")

    def input_st_info(self):
        self.st_name = input("Ten sinh vien: ")
        self.st_dob = input("Birthday: ")
        self.st_sex = input("Gioi tinh: ")
        self.st_address = input("Dia chi: ")
        self.st_mobile = input("So dien thoai: ")
        self.st_email = input("Email: ")        


    def add_student(self):
        # input information from keyboard
        print("***********Nhap thong tin sinh vien**********")
        self.st_ID = input('Ma SV: ')
        self.input_st_info()
        st_infor_str = '|'.join([self.st_ID, self.st_name, self.st_dob, self.st_sex, self.st_address, self.st_email, self.st_mobile, '\n'])
        add_st_status = write_txt_file('data/hocvien.txt', [st_infor_str], 'a+' )
        if add_st_status:
            print("Cap nhat thong tin sinh vien thanh cong")
        else:
            print("Cap nhat thong tin sinh vien khong thanh cong")


    def update_student(self):
        print("********* Nhap vao ma Sinh vien can cap nhat thong tin **********")
        while True:
            st_ID_input = input("Ma Sinh Vien: ")
            st_infors = read_txt_file('data/hocvien.txt')
            # get list of ma sv
            st_IDs = []
            for idx, st in enumerate(st_infors):
                st_ID = st.split('|')[0]
                if st_ID_input == st_ID:
                    print("Nhap thong tin moi cua sinh vien")
                    self.input_st_info()
                    st_infor_str = '|'.join(self.st_ID, self.st_name, self.st_dob, self.st_sex, self.st_address, self.st_email, self.st_mobile)
                    st_infors[idx] == st_infor_str 
                    add_st_status = write_txt_file('data/hocvien.txt', st_infors)
                    if add_st_status:
                        print("Cap nhat thong tin sinh vien thanh cong")
                        return True
                    else:
                        print("Cap nhat thong tin sinh vien khong thanh cong")
                    return False
            print("Sinh vien khong ton tai")


    def delete_student(self):
        print("********* Nhap vao ma Sinh vien **********")
        st_ID_input = input("Ma Sinh Vien: ")
        st_infors = read_txt_file('data/hocvien.txt')
        # get list of ma sv
        for idx, st in enumerate(st_infors):
            st_ID = st.split('|')[0]
            if st_ID_input == st_ID:
                st_infors.pop(idx)
                add_st_status = write_txt_file('data/hocvien.txt', st_infors)
                if add_st_status:
                    print("Xoa thong tin sinh vien thanh cong")
                    return True
                else:
                    print("Xoa thong tin sinh vien khong thanh cong")
                return False
            print("Sinh vien khong ton tai")


    def search_student(self):
        print("********* Nhap vao ma Sinh vien **********")
        st_ID_input = input("Ma Sinh Vien: ")
        st_infors = read_txt_file('data/hocvien.txt')
        # get list of ma sv
        for idx, st in enumerate(st_infors):
            st_ID = st.split('|')[0]
            if st_ID_input == st_ID:
                print('**********Thong tin sinh vien voi ma sinh vien tim thay nhu sau ***************')
                print(f'Ma SV: {st_ID_input}')
                print(f'Ten SV: {st.split("|")[1]} ')
                print(f'Ngay sinh: {st.split("|")[2]} ')
                print(f'Dia chi: {st.split("|")[3]} ')
                print(f'So Dien Thoai: {st.split("|")[4]} ')
                print(f'Email: {st.split("|")[5]} ')
        print(f'Khong ton tai sinh vien voi ma sinh vien {st_ID_input}')

