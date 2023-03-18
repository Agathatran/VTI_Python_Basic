
from utlis import *
import time
class Score:
    def __init__(self, st_ID = '', sub_ID = '', prog_score ='', final_score ='', end_score = '') -> None:
        self.st_ID = st_ID 
        self.sub_ID = sub_ID 
        self.prog_score = prog_score 
        self.final_score = final_score
        self.end_score = end_score


    def display_menu(self):
        while True:
            print('---------------------------------------')
            print("Chon mot trong cac chuc nang ben duoi:")
            print("1. Them moi diem thi")
            print("2. Cap nhat thong tin diem thi")
            print("3. Xoa thong tin diem thi")
            print("4. Tim kiem thong tin diemthi")
            print("5. Quay lai menu truoc do")
            user_input = input("Nhap ma so chuc nang can tim")
            if user_input == "1":
                self.add_score()
            elif user_input =="2":
                self.update_score()
            elif user_input == "3":
                self.delete_score()
            elif user_input == "4":
                self.search_score()
            elif user_input == '5':
                self.statistic_score()
            elif user_input == "6":
                print("byebye")
                # time.sleep(1)
                return #tai sao lai can return o day?
            else:
                print("Vui long nhap dung ma so phim chuc nang!")


    def calculate_score(self):
        self.final_score = (int(self.prog_score) + int(self.end_score)*2)/3

    def input_score_info(self):
        # self.sub_ID = input("Nhap ma mon hoc")
        # self.st_ID = input("Nhap ten sinh vien: ")
        # self.sub_ID = input("Nhap ten mon hoc: ") 
        self.prog_score= input("Diem qua trinh: ")
        self.end_score= input("Diem ket thuc: ") 


    def add_score(self):
        # input information from keyboard
        print("******** Nhap thong tin diem thi ************")
        self.st_ID = input("Ma sinh vien: ")
        self.sub_ID = input("Ma mon hoc: ")
        self.input_score_info()
        self.calculate_score()
        score_infor_str = '|'.join([self.st_ID, self.sub_ID, self.prog_score, self.end_score, str(self.final_score), '\n'])
        add_score_status = write_txt_file('data/diemthi.txt',[score_infor_str], 'a+')
        if add_score_status:
            print("Them moi diem thi thanh cong")
        else:
            print("Them moi diem thi khong thanh cong")

    def update_score(self):
        print("*********** Nhap vao ma mon hoc va ma mon hoc der cap nhat thong tin diem thi*******")
        while True:
            sub_ID_input = input("Ma mon hoc")
            st_ID_input = input("Nhap ma hoc vien")
            score_infors = read_txt_file('data/diemthi.txt')
            #print(f'subject\'s infors: {sub_infors}')
            #sub_IDs = []
            for idx, sco in enumerate(score_infors):
                st_Id = sco.split("|")[0]
                sub_ID = sco.split('|')[1]
                # print(f'sub_ID: {sub_ID}}')
                if (sub_ID_input == sub_ID) and (st_ID_input== st_Id):
                    #print("Nhap diem qua trinh va diem ket thuc mon hoc: ")
                    self.input_score_info()
                    self.calculate_score()
                    score_infor_str = '|'.join([st_Id, sub_ID_input, self.prog_score, self.end_score, str(self.final_score), '\n'])
                    score_infors[idx] = score_infor_str 

                    # print(f'sub_infors:{sub_infors}')
                    update_score_stt = write_txt_file('data/diemthi.txt',score_infors,'w+')
                    if update_score_stt:
                        print("Nhap thong tin diem thi thanh cong")
                        return True
                    else:
                        print("Nhap thong tin diem thi khong thanh cong")
                        return False
                print("Diem thi khong ton tai trong danh sach. Vui long chon diem thi khac de cap nhat.")


    def delete_score(self):
        while True:
            print("Nhap vao ma mon hoc va ma sinh vien can xoa")
            st_ID_input = input("Ma hoc vien")
            sub_ID_input = input("Ma mon hoc:")
            score_infors = read_txt_file("data/diemthi.txt")

            for idx, sco in enumerate(score_infors):
                st_Id = sco.split('|')[0]
                sub_Id = sco.split('|')[1]
                # print(f'sub_Id: {sub_Id}')
                if (st_ID_input == st_Id) and (sub_ID_input == sub_Id):
                    score_infors.pop(idx)
                    del_sub_status = write_txt_file('data/diemthi.txt',score_infors, 'w+')
                if del_sub_status:
                    print("Xoa diem thi thanh cong")
                    return True
                else:
                    print("Xoa diem thi khong thanh cong")
                    return False
            print("Diem thi khong ton tai trong danh sach.")

    def search_score(self):
        print("************** Nhap thong tin mon hoc can tim kiem ***********")
        sub_Id_input = input("Ma mon hoc")
        st_Id_input = input("Nhap vao ma hoc vien:")
        score_infors = read_txt_file("data/diemthi.txt")
        for sco in score_infors:
            st_Id = sco.split('|')[0]
            sub_Id = sco.split('|')[1]
            if (sub_Id_input == sub_Id) and (st_Id_input == st_Id):
                print('******** thong tin diem thi tim thay nhu sau: *************')
                print(f'Ma hoc vien: {st_Id}')
                print(f'Ma mon hoc: {sub_Id}')
                print(f"Diem qua trinh: {sco.split('|')[2]}")
                print(f"Diem tong ket: {sco.split('|')[3]}")
                return
            else:
                print("Khong ton tai mon hoc can tim")


    def statistic_score(self):
        score_a, score_b, score_c, score_d = [], [], [], []
        score_infors = read_txt_file('data/diemthi.txt')
        for sco in score_infors:
            fi_score = float(sco.split('|')[4])
            if fi_score >=90 and fi_score <=100:
                score_a.append(fi_score)
            elif fi_score >=70 and fi_score <90:
                score_b.append(fi_score)
            elif fi_score >=50 and fi_score <70:
                score_c.append(fi_score)
            else:
                score_d.append(fi_score)
        score_a_str = "Number of score A: " + str(len(score_a))
        score_b_str = "Number of score B: " + str(len(score_b))
        score_c_str = "Number of score C: " + str(len(score_c))
        score_d_str = "Number of score D: " + str(len(score_d))
        score_statistic = ('\n').join([score_a_str, score_b_str, score_c_str, score_d_str])
        if write_txt_file('data/score_statistic.txt', score_statistic, 'w'):
            print("Write statistic score into txt file successfully")
        else:
            print("Write statistic score into txt file unsuccessfully")
