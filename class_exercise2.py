'''
Bài 2:
Tạo một class Math_Operation:
- Có 2 thuộc tính là value_1 và value_2. Hai thuộc tính này được gán giá trị khởi tạo lúc đầu
- Có các phương thức private:
 + Phương thức 1: Kiểm tra kiểu dữ liệu của 2 thuộc tính bên trên
 + Phương thức 2: Tính tổng 2 thuộc tính nếu có thể. NẾu không thể thì in ra thông báo lỗi
 + Phương thức 3: Nếu 2 thuộc tính có kiểu list (cùng số phần tử) thì tạo ra một list thứ 3 bằng cách cộng các phần tử tương ứng của list
 + Phươpng thức 4: Nếu 2 thuộc tính có kiểu string (cùng số lượng kí tự) thì tạo ra một string thứ 3 bằng cách xen kẽ từng kí tự của 2 string
- Có các phương thức public sau:
 + Phương thức 5: Gán giá trị mới cho 2 thuộc tính bằng các giá trị nhập từ bàn phím
 + Phương thức 6: Hiển thị tổng của 2 thuộc tính
 + Phương thức 7: Hiển thị list thứ 3 trong trường hợp 2 thuộc tính có kiểu list
 + Phương thức 8: Hiển thị string thứ 3 trong trường hợp 2 thuộc tính có kiểu string
 2. Viết hàm main() bên ngoài class để thực hiện các yêu cầu sau:
- Tạo một đối tượng của class Math_Operation:
- Hiển thị tổng của 2 thuộc tính của đối tượng vừa tạo.
- Gán giá trị mới cho 2 thuộc tính của đối tượng là 2 list có cùng số lượng phần tử. Sau đó hiển thị list thứ 3.
- Gán giá trị mới cho 2 thuộc tính của đối tượng là 2 string có cùng số lượng ký tự. Sau đó hiển thị string thứ 3.
'''
class Math_Operation:
    def __init__(self, value_1, value_2):
        self.value_1 = value_1
        self.value_2 = value_2

    def __func_1(self):
        print(f'Type of value_1: {type(self.value_1)}')
        print(f'Type of value_2: {type(self.value_2)}')

    def __func_2(self):
        try:
            sum = self.value_1 + self.value_2
        except TypeError:
            print("Type Error!")
        
    def __func_3(self):
        if ((isinstance(self.value_1,list)) and (isinstance(self.value_2,list)) and (len(self.value_1)==len(self.value_2))):
            list_3= [x1+x2 for (x1, x2) in zip(self.value_1, self.value_2)]
        else:
            print("Cannot create new list")

#Phươpng thức 4: Nếu 2 thuộc tính có kiểu string (cùng số lượng kí tự) thì tạo ra một string thứ 3 bằng cách xen kẽ từng kí tự của 2 string
    def __func_4(self):
        if (isinstance(self.value_1,str) and isinstance(self.value_2,str)):
            lst1=self.value_1.split()
            lst2 = self.value_2.split()
            newlst=[i+j for (i,j) in zip(lst1,lst2)]
            newstr = ''.join(newlst)
            print(f'The new list is: {newstr}')

#Phương thức 5: Gán giá trị mới cho 2 thuộc tính bằng các giá trị nhập từ bàn phím
    def func_5(self, value_1_, value_2_):
        self.value_1 = value_1_
        self.value_2 = value_2_
        return self.value_1, self.value_2

# Phương thức 6: Hiển thị tổng của 2 thuộc tính
    def func_6(self):
        sum = self.value_1 + self.value_2
        return sum 

# Phương thức 7: Hiển thị list thứ 3 trong trường hợp 2 thuộc tính có kiểu list
    def func_7(self):
        if ((isinstance(self.value_1,list)) and (isinstance(self.value_2,list)) and (len(self.value_1)==len(self.value_2))):
            list_3= [x1+x2 for (x1, x2) in zip(self.value_1, self.value_2)]
        else:
            print("Cannot create new list")

# Phương thức 8: Hiển thị string thứ 3 trong trường hợp 2 thuộc tính có kiểu string
    def func_8(self):
        if (isinstance(self.value_1,str) and isinstance(self.value_2,str)):
            lst1=self.value_1.split()
            lst2 = self.value_2.split()
            newlst=[i+j for (i,j) in zip(lst1,lst2)]
            newstr = ''.join(newlst)
            print(f'The new list is: {newstr}')