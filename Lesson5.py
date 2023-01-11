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
#[DONE]Bài 2. Định nghĩa hàm kiểm tra xem một số từ bàn phím có phải là số chính phương hay không.
'''def checking_square(n):
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
#[DONE]Bài 3. Xác định hàm nhận vào 3 đối số, sau đó kiểm tra xem có tồn tại tam giác được tạo bởi chúng hay không. Trả lại kết quả.
'''def triangle(a,b,c):
    if ((a<=0) or (b<=0) or (c<=0)):
        print("Input numbers cannot make a triangle")
    elif ((b+c>a) and (a+c>b) and (a+b>c)):
        print("Input numbers make a triangle")
    else:
        print("Input numbers cannot make a triagle")
triangle(3,4,5)'''

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

#[DONE] Bài 6. Định nghĩa một hàm nhận vào đối số bán kính và trả về diện tích và chu vi.
'''def circle(r):
    print("The radius is: ", 3.14*r*r)
    print("The perimeter is: ", 2*3.14*r)
circle(1)'''
#Bài 7. Định nghĩa một hàm nhận vào 2 đối số: đối số thứ nhất là danh sách các số nguyên,
# đối số thứ hai là một số có giá trị mặc định là 3.
#Lặp lại danh sách theo giá trị của tham số thứ 2
# sau đó tính giá trị trung bình ủa tất cả các mục trong danh sách.

def calculate(lst,n=3):
    lst1=str(lst).split(' ')
    for i in range(0,n+1):
        print(lst1)
    for j in range(0,len(lst1)):
        lst1[j]=int(lst[j])
        tong=sum(lst1)
        ave=tong/len(lst1)
    print(ave)
calculate("12 13 14")

