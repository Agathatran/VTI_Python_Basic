from utlis import *
class lib_main():
    def __init__(self, book_Id = '', book_name = '') -> None:
        self.book_Id = book_Id
        self.book_name = book_name
    
    def display_menu(self):
        while True:
            print("************Chao mung den voi ung dung quan ly thu vien***********")
            print("vui long lua chon cac phim chuc nang duoi day.")
            print("1. Xem danh muc sach")
            print("2. Them moi vao danh muc sach")
            print("3. Cap nhat thong tin cua sach vao trong danh muc sach")
            print("4. Xoa thong tin khoi danh muc sach")
            print("5. Tim kiem thong tin sach trong danh muc theo tu khoa")
            print("6. Sap xep thong tin sach trong danh muc sach")
            user_input = input("Lua chon phim: ")
            if user_input == "1":
                pass
            elif user_input == "2":
                self.add_book()
            elif user_input == "3":
                self.update_book()
            elif user_input == "4":
                self.del_book()
            elif user_input =="5":
                self.search_book()
            elif user_input =="6":
                pass
            elif user_input =="7":
                print("Ket thuc chuong trinh")
                return
            else:
                print("Vui long chon dung phim chuc nang!")
    def input_book_info(self):
        self.book_name = input("Nhap ten sach: ")

    def add_book(self):
        # input information from keyboard
        print("******* Nhap thong tin sach ********")
        self.book_Id = input("Nhap ma sach: ")
        self.input_book_info()
        book_info_str = '|'.join([self.book_Id, self.book_name])
        add_book_stt = write_txt_file('book.txt',[book_info_str], 'a+')
        if add_book_stt:
            print("Them sach thanh cong")
        else:
            print("Them sach khong thanh cong")

    def update_book(self):
        print("******* Nhap vao ten sach can cap nhat *********")
        while True:
            book_name_input = input("Ten sach")
            book_info = read_txt_file('book.txt')
            book_names = []
            for idx, st in enumerate(book_info):
                book_name = st.split('|')[1]
                if book_name == book_name_input:
                    print("Nhap thong tin sach moi")
                    self.input_book_info()
                print("Sinh vien khong ton tai")
    
    def del_book(self):
        print("********* Nhap vao ten sach *********")
        book_name_input = input("Nhap vao ten sach")
        book_info = read_txt_file('book.txt')
        for idx, st in enumerate(book_info):
            book_name = st.split('|')[1]
            if book_name == book_name_input:
                book_info.pop(idx)
                add_book_stt = write_txt_file('book.txt', book_info)
                if add_book_stt:
                    print("Xoa thong tin sach thanh cong")
                    return True
                else:
                    print("Xoa thong tin sach khong thanh cong")
                return False 
            print("Sach khong ton tai")

    def search_book(self):
        print("********* Nhap vao ten sach **********")
        book_name_input = input("Ten sach: ")
        book_info = read_txt_file('book.txt')
        # get list of ma sv
        for idx, st in enumerate(book_info):
            book_name = st.split('|')[1]
            if book_name == book_name_input:
                print('**********Thong tin sach tim thay nhu sau ***************')
                print(f'Ma sach: {st.split("|")[0]}')
                print(f'Ten sach: {st.split("|")[1]} ')

        print(f'Khong ton tai sach voi ten sach {book_name_input}')


main = lib_main()
main.display_menu()





