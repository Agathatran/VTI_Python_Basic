#from txt_file_ops import *
from utils.db_conn import *
from objects.base_class import *
from loguru import logger
from tabulate import tabulate
from datetime import datetime

class Student(Base_CLS):
    def __init__(self, st_ID='', st_name='', st_dob='', st_sex='', st_address='', st_mobile='', st_email='') -> None:
        self.__st_ID = st_ID
        self.__st_name = st_name
        self.__st_dob = st_dob
        self.__st_sex = st_sex
        self.__st_address = st_address
        self.__st_mobile = st_mobile
        self.__st_email = st_email
        db_obj = MySQLConn()
        self.__db_conn = db_obj.create_conn()
        self.__db_cur = self.__db_conn.cursor()
        
    def display_menu(self):
        while True:
            print('---------------------------------')
            print('Chon 1 trong cac chuc nang ben duoi:')
            print('0. Hien thi thong tin 5 sinh vien')
            print('1. Them moi sinh vien')
            print('2. Cap nhap thong tin sinh vien')
            print('3. Xoa thong tin sinh vien')
            print('4. Tim kiem thong tin sinh vien')
            print('5. Quay lai menu truoc do')

            user_input = input('Chon chuc nang: ')
            if user_input == '0':
                self.__get_data()
            elif user_input == '1':
                self.__add_data()
            elif user_input == '2':
                self.__update_data()
            elif user_input == '3':
                self.__delete_data()
            elif user_input == '4':
                self.__search_data()
            elif user_input == '5':
                print('BYE BYE')
                # time.sleep(1)
                return
            else:
                print('Vui long nhap dung ma so chuc nang quy dinh')
    


    def __get_data(self): 
        sql_command = "SELECT * FROM Students LIMIT 5"
        self.__db_cur.execute(sql_command)
        result = self.__db_cur.fetchall()
        list_st = []
        for idx, row in enumerate(result):
            # logger.info(row)
            st_info = [row[0], row[1], row[2], row[3], row[4], row[5]]
            list_st.append(st_info)

        print(tabulate(list_st, headers=["Ma SV","Ngay Sinh", "Dia Chi", "So DT", "Email"], numalign="left"))

    def __input_st_info(self):
        self.__st_name = input('Ten SV: ')
        self.__st_dob = input('Ngay sinh: ')
        # self.st_sex = input('Gioi tinh: ')
        self.__st_address = input('Dia chi: ')
        self.__st_mobile = input('So dien thoai: ')
        self.__st_email = input('Email: ')

    def __validate_data(self):
        is_error = False
        # validate name
        if len(self.__st_name) <= 0 or len(self.__st_name) > 30:
            logger.error('Chieu dai cua ten khong duoc nho hon khong va lon hon 30. Vui long nhap lai!')
            is_error = True

        # validate date of birth
        format = "%Y-%m-%d"
        # using try-except to check for truth value
        try:
            bool(datetime.strptime(self.__st_dob, format))
        except ValueError:
            logger.error('Vui long nhap dung dinh dang ngay sinh: %Y-%m-%d')
            is_error = True

        # validate phone number
        if len(self.__st_mobile) > 11 or len(self.__st_mobile) < 10:
            logger.error('Chieu dai so dien thoai trong khoang 10-11! Vui long kiem tra lai!')
            is_error = True
        if (not self.__st_mobile.isdigit()):
            logger.error('So dien thoai chi duoc phep bao gom cac ky tu so! Vui long kiem tra lai!')
            is_error = True

        # validate email
        if not self.__st_email.__contains__('@'):
            logger.error('Email phai bao gom ky tu @. Vui long kiem tra lai!')
            is_error = True

        return is_error

    def __add_data(self):
        # input information from keyboard
        print('*********** Nhap thong tin sinh vien ***********')
        self.__input_st_info()
        if self.__validate_data():
            return
        
        # insert data to db
        sql_cmd = """
            INSERT INTO Students(Name, DoB, Address, Phone_Number, Email)
            VALUES (%s, %s, %s, %s, %s)
        """
        # vals = ("Đỗ Duy Hiệu", '2002-10-20', 'Bac Ninh', '0988764343', "duyhieu@gmail.com")
        vals = (self.__st_name, self.__st_dob, self.__st_address, self.__st_mobile, self.__st_email)
        self.__db_cur.execute(sql_cmd, vals)
        self.__db_conn.commit()
        logger.info('Them moi sinh vien thanh cong!')

    def __update_data(self):
        print('************ Nhap vao Ma SV can cap nhat thong tin *************')
        st_Id_input = int(input('Ma SV: '))
        self.__input_st_info()
        sql_cmd = "UPDATE Students SET Name= %s, DoB=%s, Address=%s, Phone_Number=%s, Email=%s WHERE ST_Id=%s"
        self.db_cur.execute(sql_cmd, (self.__st_name, self.__st_dob, self.__st_address, self.__st_mobile, self.__st_email, st_Id_input))
        if(self.__db_conn.commit()):
            logger.info('Cap nhat thong tin sinh vien khong thanh cong. Vui long thu lai sau!')
        else:
            logger.info('Cap nhat thong tin sinh vien thanh cong.')


    def __delete_data(self):
        print('************ Nhap vao Ma SV *************')
        st_Id_input = input('Ma SV: ')
        sql_cmd = "DELETE FROM Students WHERE ST_Id=%s"
        self.__db_cur.execute(sql_cmd, [st_Id_input])
        if(self.__db_conn.commit()):
            logger.info('Xoa thong tin sinh vien khong thanh cong. Vui long thu lai sau!')
        else:
            logger.info('Xoa thong tin sinh vien thanh cong.')
            

    def __search_data(self):
        print('************ Nhap vao Ma SV *************')
        st_Id_input = input('Ma SV: ')
        sql_cmd = "SELECT * FROM Students WHERE ST_Id=%s"
        self.__db_cur.execute(sql_cmd, [st_Id_input])
        results = self.__db_cur.fetchall()
        for row in results:
            # logger.info(row)
            print('*********** Thong tin sinh vien tim thay nhu sau: ************ ')
            print(f'Ma SV: {st_Id_input}')
            print(f'Ho ten: {row[1]}')
            print(f'Ngay sinh: {row[2]}')
            # print(f'Gioi tinh: {row[3]}')
            print(f'Dia chi: {row[3]}')
            print(f'So dien thoai: {row[4]}')
            print(f'Email: {row[5]}')