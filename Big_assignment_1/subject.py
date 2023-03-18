
from utlis import *
import time
class subject:
    def __init__(self, sub_ID = '', sub_name ='') -> None:
        self.sub_ID = sub_ID
        self.sub_name = sub_name

    def display_menu(self):
        while True:
            print('---------------------------------------')
            print("Chon mot trong cac chuc nang ben duoi:")
            print("1. Them moi mon hoc")
            print("2. Cap nhat thong tin mon hoc")
            print("3. Xoa thong tin mon hoc")
            print("4. Tim kiem thong tin mon hoc")
            print("5. Quay lai menu truoc do")
            user_input = input("Nhap ma so chuc nang can tim")
            if user_input == "1":
                self.add_subject()
            elif user_input =="2":
                self.update_subject()
            elif user_input == "3":
                self.delete_sub()
            elif user_input == "4":
                self.search_subject()
            elif user_input == "5":
                print("byebye")
                time.sleep(1)
                return #tai sao lai can return o day?
            else:
                print("Vui long nhap dung ma so phim chuc nang!")


    def input_sub_info(self):
        # self.sub_ID = input("Nhap ma mon hoc")
        self.sub_name = input("Nhap ten mon hoc")       


    def add_subject(self):
        # input information from keyboard
        print("******** Nhap thong tin mon hoc ************")
        self.sub_ID = input("Ma mon hoc")
        self.input_sub_info()
        sub_infor_str = '|'.join([self.sub_ID, self.sub_name])
        add_sub_status = write_txt_file('data/monhoc.txt',[sub_infor_str], 'a+')
        if add_sub_status:
            print("Them mon hoc thanh cong")
        else:
            print("Them mon hoc khong thanh cong")

    def update_subject(self):
        print("*********** Nhap vao ma mon hoc can cap nhat*******")
        while True:
            sub_ID_input = input("Ma mon hoc")
            sub_infors = read_txt_file('data/monhoc.txt')
            print(f'subject\'s infors: {sub_infors}')
            #sub_IDs = []
            for idx, sub in enumerate(sub_infors):
                sub_ID = sub.split("|")[0]
                print(f'sub_ID: {sub_ID}')
                if sub_ID_input == sub_ID:
                    print("Nhap thong tin mon hoc moi")
                    self.input_sub_info()
                    sub_infor_str = '|'.join([self.sub_ID, self.sub_name, '\n'])
                    sub_infors[idx] = sub_infor_str 
                    print(f'sub_infors:{sub_infors}')
                    update_sub_stt = write_txt_file('data/monhoc.txt',sub_infor_str,'w+')
                    if update_sub_stt:
                        print("Nhap thong tin mon hoc thanh cong")
                        return True
                    else:
                        print("Nhap thong tin mon hoc khong thanh cong")
                        return False
                print("Mon hoc khong ton tai.")


    def delete_sub(self):
        while True:
            print("Nhap vao ma mon hoc can xoa")
            sub_ID_input = input("Ma mon hoc")
            sub_infors = read_txt_file("data/monhoc.txt")
            for idx, sub in enumerate(sub_infors):
                sub_Id = sub.split('|')[0]
                print(f'sub_Id: {sub_Id}')
                if sub_ID_input == sub_Id:
                    sub_infors.pop(idx)
                    del_sub_status = write_txt_file('data/monhoc.txt',sub_infors, 'w+')
                if del_sub_status:
                    print("Xoa mon hoc thanh cong")
                    return True
                else:
                    print("Xoa mon hoc khong thanh cong")
                    return False
            print("Mon hoc khong ton tai trong danh sach.")

    def search_subject(self):
        print("************** Nhap thong tin mon hoc can tim kiem ***********")
        sub_search_ID = input("Nhap ma mon hoc can tim kiem")
        sub_infors = read_txt_file("data/monhoc.txt")
        for id, sub_search in enumerate(sub_infors):
            id_search = sub_search.split('|')[0]
            if sub_search_ID == id_search:
                print(f"Thong tin mon hoc can tim kiem la: {id_search, sub_search.split('|')[1]}")
            else:
                print("Khong ton tai mon hoc can tim")

    def search_subject(self):
        print("*********** Nhap vao ma mon hoc *********")
        sub_ID_input = input("Ma mon hoc")
        sub_infors = read_txt_file('data/monhoc.txt')
        for sub in sub_infors:
            sub_ID = sub.split('|')[0]
            if sub_Id_input == sub_Id:
                print("Thong tin mon hoc tim thay nhu sau: ")
                print(f'Ma mon hoc: {sub_ID}')
                print(f'Ten mon hoc: {sub.split("|")[1]}')
                return 
            print(f'Kong ton tai mon hoc voi ma mon hoc {sub_ID_input}')