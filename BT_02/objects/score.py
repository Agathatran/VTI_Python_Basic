from utils.db_conn import *
from objects.base_class import *
from loguru import logger
from tabulate import tabulate
from datetime import datetime

class Score:
    def __init__(self, st_Id='', sub_Id='', prog_score='', end_score='', final_score='') -> None:
        self.__st_Id = st_Id
        self.__sub_Id = sub_Id
        self.__prog_score = prog_score
        self.__end_score = end_score
        self.__final_score = final_score
        db_obj = MySQLConn()
        self.__db_conn = db_obj.create_conn()
        self.__db_cur = self.__db_conn.cursor()

    def display_menu(self):
        while True:
            print('---------------------------------')
            print('Chon 1 trong cac chuc nang ben duoi:')
            print('0. Hien thi thong tin cac mon hoc')
            print('1. Them moi diem thi')
            print('2. Cap nhap thong tin diem thi')
            print('3. Xoa thong tin diem thi')
            print('4. Tim kiem thong tin diem thi')
            print('5. Thong ke diem thi')
            print('6. Quay lai menu truoc do')
            user_input = input('Chon chuc nang: ')
            if user_input == '0':
                self.__get_data()
            elif user_input == '1':
                self.__add_score()
            elif user_input == '2':
                self.__update_score()
            elif user_input == '3':
                self.__delete_score()
            elif user_input == '4':
                self.__search_score()
            elif user_input == '5':
                self.__statistic_score()
            elif user_input == '6':
                print('BYE BYE')
                # time.sleep(1)
                return
            else:
                print('Vui long nhap dung ma so chuc nang quy dinh')
    
    def __get_data(self):
        sql_command = "SELECT * FROM subjects LIMITS 5"
        self.__db_cur.execute(sql_command)
        result = self.__db_cur.fetchall()
        list_st = []
        for idx, row in enumerate(result):
            st_info = [row[0], row[1], row[2], row[3], row[4], row[5]]
            list_st.append(st_info)
            print(tabulate(list_st, headers=["Ma Mon hoc","Ten mon hoc", "Diem qua trinh", "Diem cuoi ky", "Diem ket thuc"], numalign="center"))


    def __cal_final_score(self):
        self.__final_score = (int(self.__prog_score) + int(self.__end_score)*2)/3

    def __input_score_info(self):
        # self.st_Id = input('Ten Sinh vien: ')
        # self.sub_Id = input('Ten Mon hoc: ')
        self.__prog_score = input('Diem qua trinh: ')
        self.__end_score = input('Diem ket thuc: ')

    def __validate_data(self):
        is_error = False
        #valid prog_score
        if (self.__prog_score < 0) or (self.__prog_score > 100):
            logger.info('Diem thi phai nam trong khoang tu 0 den 100. Vui long nhap lai!')
            is_error = True
        #valid end_score
        if (self.__end_score < 0) or (self.__end_score >100):
            logger.info('Diem thi phai nam trong khoang tu 0 den 100. Vui long nhap lai!')
            is_error = True
        return is_error



    def __add_score(self):
        # input information from keyboard
        print('*********** Nhap thong tin diem thi ***********')
        self.st_Id = input('Ma Hoc vien: ')
        self.sub_Id = input('Ma Mon hoc: ')
        self.__input_score_info()
        if self.__validate_data():
            return
        self.__cal_final_score()
        #insert data to db
        sql_cmd ="""
                    INSERT INTO scores(Pro_sco, end_score)
            VALUES (%s, %s)
        """
        vals = (self.__st_Id, self.__sub_Id, self.__prog_score, self.__final_score, self.__end_score)
        self.__db_cur.execute(sql_cmd,vals)
        self.__db_conn.commit()
        logger.info("Them moi diem thi thanh cong")


        # format data. 
        # For example: 
        # PY000005|Nguyễn Phương Thảo|08/09/1995|0|Hà Nội|0964330956|nguyenthao.npt98@gmail.com
        # score_infor_str = '|'.join([self.st_Id, self.sub_Id, self.prog_score, self.end_score, str(self.final_score), '\n'])
        # add_score_status = write_txt_file('data/diemthi.txt', [score_infor_str], 'a+')
        # if add_score_status:
        #     print('Them moi diem thi thanh cong')
        # else:
        #     print('Them moi diem thi khong thanh cong')

    def __update_score(self):
        while True:
            print('************ Nhap vao Ma mon hoc va Ma hoc vien de cap nhat thong tin diem thi *************')
            sub_Id_input = input('Ma Mon hoc: ')
            st_Id_input = input('Ma Hoc vien: ')
            self.__input_score_info()
            sql_cmd = """"UPDATE Students SET prog_score= %s, final_score=%s, end_score=%s WHERE (ST_Id=%s AND Sub_Id = %s)"""
            self.__db_cur.execute(sql_cmd, (self.__prog_score, self.__final_score, self.__end_score))
            if(self.__db_conn.commit()):
                logger.info('Cap nhat thong tin diem thi khong thanh cong. Vui long nhap lai diem thi!')
            else:
                logger.info('Cap nhat thong tin diem thi thanh cong.')
            print('Diem thi khong ton tai trong danh sach. Vui long chon diem thi khac de cap nhat')



            #score_infors = read_txt_file('data/diemthi.txt')
            # print(f'sub_infors: {sub_infors}')
            # get list of ma sv
            # for idx, sco in enumerate(score_infors): 
            #     st_Id = sco.split('|')[0]  
            #     sub_Id = sco.split('|')[1]
                # print(f'sub_Id: {sub_Id}')
               # if sub_Id_input == sub_Id and st_Id_input == st_Id:
                #     # print('Nhap diem qua trinh va diem ket thu:')
                #     self.input_score_info()
                #     self.cal_final_score()
                #     # format data. 
                #     # For example: 
                #     # PY000005|Nguyễn Phương Thảo|08/09/1995|0|Hà Nội|0964330956|nguyenthao.npt98@gmail.com
                #     score_infor_str = '|'.join([st_Id, sub_Id_input, self.prog_score, self.end_score, str(self.final_score), '\n'])
                #     # print(f'score_infor_str: {score_infor_str}')
                #     score_infors[idx] = score_infor_str
                #     # print(f'sub_infors: {sub_infors}')
                #     update_score_status = write_txt_file('data/diemthi.txt', score_infors, 'w+')
                #     if update_score_status:
                #         print('Cap nhat thong tin diem thi thanh cong')
                #         return True
                #     else:
                #         print('Cap nhat thong tin diem thi khong thanh cong. Vui long thu lai sau')
                #         return False
                    
           


    def __delete_score(self):
        while True:
            print('************ Nhap vao Ma Hoc vien va Ma Mon hoc *************')
            sub_Id_input = input('Ma Mon hoc: ')
            st_Id_input = input('Ma Hoc vien: ')
            sql_cmd = "DELETE FROM student_db.scores WHERE (St_Id = %s AND Sub_Id = %s)"
            self.__db_cur.execute(sql_cmd, [st_Id_input])
            if(self.__db_conn.commit()):
                logger.info('Xoa thong tin diem thi khong thanh cong. Vui long thu lai sau!')
            else:
                logger.info('Xoa thong tin diem thi thanh cong.')
            
            print('Diem thi khong ton tai trong danh sach. Vui long nhap thong tin khac')

            #score_infors = read_txt_file('data/diemthi.txt')
            # get list of ma sv
            # for idx, sco in enumerate(score_infors):   
            #     st_Id = sco.split('|')[0]  
            #     sub_Id = sco.split('|')[1]
            #     # print(f'sub_Id: {sub_Id}')
            #     if sub_Id_input == sub_Id and st_Id_input == st_Id:
            #         score_infors.pop(idx)
            #         del_score_status = write_txt_file('data/diemthi.txt', score_infors, 'w+')
            #         if del_score_status:
            #             print('Xoa thong tin diem thi thanh cong')
            #             return True
            #         else:
            #             print('Xoa thong tin diem thi khong thanh cong. Vui long thu lai sau')
            #             return False
           

    def __search_score(self):
        print('************ Nhap vao Ma Hoc vien va Ma Mon hoc *************')
        sub_Id_input = input('Ma Mon hoc: ')
        st_Id_input = input('Ma Hoc vien: ')
        sql_cmd = "SELECT * FROM student_db.scores WHERE (St_Id = %s AND sub_Id = %s)"
        self.__db_cur.execute(sql_cmd,[st_Id_input])
        results = self.__db_cur.fetchall()
        for row in results:
            print('*********** Thong tin diem thi tim thay nhu sau: ************ ')
            print(f'Ma SV: {st_Id_input}')
            print(f'Ma mon hoc: {row[1]}')
            print(f'Diem qua trinh: {row[2]}')
            # print(f'Gioi tinh: {row[3]}')
            print(f'Diem cuoi ki: {row[3]}')
            print(f'Diem tong ket: {row[4]}')
           # print(f'Email: {row[5]}')

        # score_infors = read_txt_file('data/diemthi.txt')
        # # get list of ma sv
        # for sco in score_infors:   
        #     st_Id = sco.split('|')[0]  
        #     sub_Id = sco.split('|')[1]

        #     if sub_Id_input == sub_Id and st_Id_input == st_Id:
        #         print('*********** Thong tin diem thi tim thay nhu sau: ************ ')
        #         print(f'Ma Hoc vien: {st_Id}')
        #         print(f'Ma Mon hoc: {sub_Id}')
        #         print(f'Diem qua trinh: {sco.split("|")[2]}')
        #         print(f'Diem tong ket: {sco.split("|")[3]}')
        #         return
        print(f'Khong ton tai diem thi voi ma hoc vien {st_Id_input} va ma mon hoc {sub_Id_input}!')

    def __statistic_score(self):
        score_a, score_b, score_c, score_d = [], [], [], []
        score_infors = read_txt_file('data/diemthi.txt')
        for sco in score_infors:
            fi_score = float(sco.split('|')[4])
            if fi_score >= 90 and fi_score <= 100:
                score_a.append(fi_score)
            elif fi_score >= 70 and fi_score < 90:
                score_b.append(fi_score)
            elif fi_score >= 50 and fi_score < 70:
                score_c.append(fi_score)
            else:
                score_d.append(fi_score)
        
        score_a_str = "Number of score A: " + str(len(score_a))
        score_b_str = "Number of score B: " + str(len(score_b))
        score_c_str = "Number of score C: " + str(len(score_c))
        score_d_str = "Number of score D: " + str(len(score_d))
        score_statistic = ('\n').join([score_a_str, score_b_str, score_c_str, score_d_str])
        if write_txt_file('data/score_statistic.txt', score_statistic, 'w+'):
            print('Write statistic score into txt file sucessfully')
        else:
            print('Write statistic score into txt file not sucessfully')