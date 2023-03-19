from utils.db_conn import *
from objects.base_class import *
from loguru import logger
from tabulate import tabulate
from datetime import datetime

class Subject:
    def __init__(self, sub_id='', sub_name='') -> None:
        self.__sub_id = sub_id
        self.__sub_name = sub_name

    def display_menu(self):
        while True:
            print('---------------------------------')
            print('Chon 1 trong cac chuc nang ben duoi:')
            print('0. Hien thi thong tin 5 mon hoc')
            print('1. Them moi mon hoc')
            print('2. Cap nhap thong tin mon hoc')
            print('3. Xoa thong tin mon hoc')
            print('4. Tim kiem thong tin mon hoc')
            print('5. Quay lai menu truoc do')
            user_input = input('Chon chuc nang: ')
            if user_input =='0':
                self.__getdata()
            elif user_input == '1':
                self.__add_subject()
            elif user_input == '2':
                self.__update_subject()
            elif user_input == '3':
                self.__delete_subject()
            elif user_input == '4':
                self.__search_subject()
            elif user_input == '5':
                print('BYE BYE')
                # time.sleep(1)
                return
            else:
                print('Vui long nhap dung ma so chuc nang quy dinh')

    def __get_data(self):
        sql_command = "SELECT * FROM student_db.subjects LIMIT 5"
        self.__db_cur.execute(sql_command)
        result = self.__db_cur.fetchall()
        list_st=[]
        for idx, row in enumerate(result):
            st_info = [row[0], row[1]]
            list_st.append(sub_info)
        print(tabulate(list_st, headers=["Ma mon hoc","Mon hoc"], numalign="left"))

    def __input_sub_info(self):
        self.sub_name = input('Ten Mon hoc: ')

    def __validate_data(self):
        is_error = False
        #validate name
        if len(self.__sub_name) <= 0 or len(self.__sub_name) > 30:
            logger.error('Chieu dai cua ten khong duoc nho hon khong va lon hon 30. Vui long nhap lai!')
            is_error = True
        return is_error

    def __add_subject(self):
        # input information from keyboard
        print('*********** Nhap thong tin mon hoc ***********')
        # self.sub_id = input('Ma Mon hoc: ')
        self.__input_subject_info()
        if self.__validate_data():
            return 
        sql_cmd = """
            INSERT INTO student_db.subjects(Name)
            VALUES (%s)
        """
        vals = self.__sub_name
        self.__db_cur.execute(sql_cmd, vals)
        self.__db_conn.commit()
        logger.info('Them moi mon hoc thanh cong!')
     


        # format data. 
        # For example: 
        # PY000005|Nguyễn Phương Thảo|08/09/1995|0|Hà Nội|0964330956|nguyenthao.npt98@gmail.com
        # sub_infor_str = '|'.join([self.sub_id, self.sub_name, '\n'])
        # add_sub_status = write_txt_file('data/monhoc.txt', [sub_infor_str], 'a+')
        # if add_sub_status:
        #     print('Them moi mon hoc thanh cong')
        # else:
        #     print('Them moi mon hoc khong thanh cong')

    def __update_subject(self):
        while True:
            print('************ Nhap vao Ma mon hoc can cap nhat thong tin *************')
            sub_Id_input = int(input('Ma Mon hoc: '))
            self.__input_sub_info()
            sql_cmd = "UPDATE subjects  SET Name = %s WHERE Sub_Id = %s"
            self.db_cur.execute(sql_cmd, (self.__sub_name))
            if(self.__db_conn.commit()):
                logger.info('Cap nhat thong tin mon hoc khong thanh cong. Vui long thu lai sau!')
            else:
                logger.info('Cap nhat thong tin mon hoc thanh cong.')
            print('Mon hoc khong ton tai trong danh sach. Vui long nhap ma sv khac')


            # sub_infors = read_txt_file('data/monhoc.txt')
            # print(f'sub_infors: {sub_infors}')
            # # get list of ma sv
            # for idx, sub in enumerate(sub_infors):   
            #     sub_Id = sub.split('|')[0]
            #     print(f'sub_Id: {sub_Id}')
            #     if sub_Id_input == sub_Id:
            #         print('Nhap ten moi cua mon hoc')
            #         self.input_subject_info()
                    # format data. 
                    # For example: 
                    # PY000005|Nguyễn Phương Thảo|08/09/1995|0|Hà Nội|0964330956|nguyenthao.npt98@gmail.com
                    # sub_infor_str = '|'.join([sub_Id_input, self.sub_name, '\n'])
                    # sub_infors[idx] = sub_infor_str
                    # print(f'sub_infors: {sub_infors}')
                    # update_sub_status = write_txt_file('data/monhoc.txt', sub_infors, 'w+')
                    # if update_sub_status:
                    #     print('Cap nhat thong tin mon hoc thanh cong')
                    #     return True
                    # else:
                    #     print('Cap nhat thong tin mon hoc khong thanh cong. Vui long thu lai sau')
                    #     return False
                    




    def __delete_subject(self):
        while True:
            print('************ Nhap vao Ma Mon hoc *************')
            sub_Id_input = input('Ma SV: ')
            sql_cmd = "DELETE FROM subjects WHERE Sub_Id=%s"
            self.__db_cur.execute(sql_cmd, [sub_Id_input])
            if(self.__db_conn.commit()):
                logger.info('Xoa thong tin mon hoc khong thanh cong. Vui long thu lai sau!')
            else:
                logger.info('Xoa thong tin mon hoc thanh cong.')
            print('Mon hoc khong ton tai trong danh sach. Vui long nhap ma mon hoc khac')
            # sub_Id_input = input('Ma Mon hoc: ')
            # sub_infors = read_txt_file('data/monhoc.txt')
            # # get list of ma sv
            # for idx, sub in enumerate(sub_infors):   
            #     sub_Id = sub.split('|')[0]
            #     print(f'sub_Id: {sub_Id}')
            #     if sub_Id_input == sub_Id:
            #         sub_infors.pop(idx)
            #         del_sub_status = write_txt_file('data/monhoc.txt', sub_infors, 'w+')
            #         if del_sub_status:
            #             print('Xoa thong tin mon hoc thanh cong')
            #             return True
            #         else:
            #             print('Xoa thong tin mon hoc khong thanh cong. Vui long thu lai sau')
            #             return False
            

    def __search_subject(self):
        print('************ Nhap vao Ma Mon hoc *************')
        st_sub_input = input('Ma mon hoc: ')
        sql_cmd = "SELECT * FROM subjects WHERE Sub_Id=%s"
        self.__db_cur.execute(sql_cmd, [st_sub_input])
        results = self.__db_cur.fetchall()
        for row in results:
            # logger.info(row)
            print('*********** Thong tin sinh vien tim thay nhu sau: ************ ')
            print(f'Ma mon hoc: {st_sub_input}')
            print(f'Ten mon hoc: {row[1]}')


        # sub_Id_input = input('Ma Mon hoc: ')
        # sub_infors = read_txt_file('data/monhoc.txt')
        # # get list of ma sv
        # for sub in sub_infors:   
        #     sub_Id = sub.split('|')[0]
        #     if sub_Id_input == sub_Id:
        #         print('*********** Thong tin mon hoc tim thay nhu sau: ************ ')
        #         print(f'Ma Mon hoc: {sub_Id}')
        #         print(f'Ten Mon hoc: {sub.split("|")[1]}')
        #         return
        print(f'Khong ton tai mon hoc voi ma mon hoc {sub_Id_input}')