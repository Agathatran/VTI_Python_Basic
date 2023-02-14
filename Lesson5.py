import math
#[DONE]Bài 1. Định nghĩa hàm nhận vào 2 giá trị và trả về tổng, phép chia, phép trừ và phép nhân (sử dụng ngoại lệ cho phép chia).
'''def calculation(x,y):
    print("Their sum is: ", x+y)
    print("Their difference is: ", x-y)
    print("Their product is: ", x*y)
    try:
            print("Their division is: ",x/y)
    except ZeroDivisionError:
        print("Can not divide by 0")
a=int(input('Input the first number: '))
b=int(input('Input the second numer: '))
calculation(a,b)'''

'''def calculate(num_1, num_2):
    sum = num_1 + num_2
    sub = num_1 - num_2
    mul = num_1 * num_2
    if num_2!=0:
        div= num_1/num_2
    else:
        div=None
    return sum, div, sub, mul
num1 = 10
num2=20
sum_, div_, mul_, sub_ =calculate (num1,num2)
print(f'Sum: {sum_}')
print(f'Sub: {sub_}')
print(f'Mul: {mul_}')
if div_:
    print(f'Div: {div_}')
else:
    print('Number2 bang 0')'''


#[DONE]Bài 2. Định nghĩa hàm kiểm tra xem một số từ bàn phím có phải là số chính phương hay không.
'''def is_square():
    num=int(input("Input a number: "))
    if n<0:
        print("Impossible")
    else:
        for i in range(n):
            if i**2==n:
                print(n," is a squared number")
                break
            else:
                print(n, "is not a squared number")
checking_square(4)'''

#Solution 1: check xem sqrt(n) có phải là integer hay không
'''def is_square():
    number=int(input("Input a positive number: "))
    if isinstance(math.sqrt(number),int)==True:
        print("Yes")
        return True
    else:
        print("No")
    return
is_square()'''

#Solution 2:Tính sqrt(n)
'''def is_square():
    number=int(input("Input a number: "))
    sq_root = int(math.sqrt(number))
    if sq_root*sq_root==number:
        print("Yes")
        return True
    print("False")
    return False

#Test function

is_square()'''


#[DONE]Bài 3. Xác định hàm nhận vào 3 đối số, sau đó kiểm tra xem có tồn tại tam giác được tạo bởi chúng hay không. Trả lại kết quả.
'''def is_valid_triangle(a,b,c):
    if ((a<=0) or (b<=0) or (c<=0)):
        print("Input numbers cannot make a triangle")
    elif ((b+c>a) and (a+c>b) and (a+b>c)):
        print("Input numbers make a triangle")
    else:
        print("Input numbers cannot make a triagle")
is_valid_triangle(3,4,5)'''
'''def is_valid_triangle(a,b,c):
    if (a+b>c) and (b+c >a) and (a+c >b):
        print(f'Yes')
        return True 
    print(f'No')
    return False 
a,b,c=10,13,9
is_valid_triangle(a,b,c)'''

#[DONE] Bài 4. Định nghĩa một hàm nhận vào một đối số chuỗi và trả về số lượng nguyên âm và phụ âm.
'''consonants=['u','e','o','a','i']
vowels=['b','c','d','f','g','h','k','l','m','n','p','q','r','s','t','v','w','y','z','x']
n=str(input("Input a string: "))
def spelling(x):
    n_cons=0
    n_vowels=0
    lst=list(n)
    for i in lst:
        if i in consonants:
             n_cons+=1
        elif i in vowels:
            n_vowels +=1
    print("The number of consonant is: ", n_cons)
    print("The number of vowel is: ", n_vowels)
spelling(n)'''
#Solution
'''def count_character(sequence):
    num_vowels =0
    num_consonants=0
    list_vowels = ['a','e','i','u','o']
    for i in sequence:
        if i.lower() in list_vowels:
            num_vowels +=1
        else:
            num_consonants +=1
    print(f'Number of vowels:{num_vowels}')
    print(f'Number of consonant:{num_consonants}')
    return num_vowels, num_consonants
#Test function
count_character('Xuan Thanh')
'''
#Solution 2: lập list_vowels ---> check .isalphabet() ---> check in list_vowels
#else: continue ---> chạy tiếp (ngược với pass)




#[DONE]Bài 5. Định nghĩa một hàm nhận vào một số (n) và trả về n số đầu tiên của dãy Fibonacci.

'''def fibonacci(n):
    f0=1
    f1=1
    fn=1
    if n==0:
        print("0")
    elif n==1:
        print("1")
    elif n<0:
        print("Input a positive number")
    else:
        for n in range(2,n+1):
            f0=f1
            f1=fn
            fn=f0+f1
        print(fn)
fibonacci(6)'''
#Solution
'''
def show_fibonaci(n):
    n1,n2=0,1
    count_fb=2
    list_fb = []
    if n==1:
        list_fb.append(n1)
    else:
        list_fb.append(n1)
        list_fb.append(n2) # nếu muốn mở rộng nhiều thì dùng extend
        while count_fb <n :
            n_th = n1+ n2
            list_fb.append(n_th)
            n1=n2
            n2=n_th
            count_fb+=1
    return list_fb
list_fb=show_fibonaci(3)
print(list_fb)
'''

#[DONE] Bài 6. Định nghĩa một hàm nhận vào đối số bán kính và trả về diện tích và chu vi.
'''def cal_circle():
    k=float(input("Input a non-negative number: "))
    perimeter = math.pi * k 
    area = math.pi * k**2
    print(f'The perimeter is: {perimeter}')
    print(f'The area is: {area}')
    return perimeter, area
cal_circle()'''
#[DONE] Bài 7. Định nghĩa một hàm nhận vào 2 đối số: đối số thứ nhất là danh sách các số nguyên,
# đối số thứ hai là một số có giá trị mặc định là 3.
#Lặp lại danh sách theo giá trị của tham số thứ 2
# sau đó tính giá trị trung bình ủa tất cả các mục trong danh sách.

'''def calculate(lst,n=3):
    lst1=str(lst).split(' ')
    for i in range(0,n+1):
        print(lst1)
    for j in range(0,len(lst1)):
        lst1[j]=int(lst1[j])
    print(lst1)
    print(sum(lst1))
    print(sum(lst1)/(len(lst1)+1))
    
calculate("1 2 14")'''

#Solution
def list_operations(list_num,n=3):
    list_num = list_num*3
    avg = sum(list_num) / len(list_num)
    return avg
#Test function
list_num= [1,2,4]
avg= list_operations(list_num)
print(f'Avg: {avg}')
