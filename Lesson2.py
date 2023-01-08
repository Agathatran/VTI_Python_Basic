#Bài 1: 
#Viết chương nhập 2 số từ bàn phím. Tính và in ra giá trị tổng, tích, hiệu, thương của chúng (có kiểm tra điều kiện)
'''
num1 = int(input('num1'))
num2 = int(input('num2'))
print(f'Sum: {num1 + num2}')
print(f'Product: {num1+num2}')
print(f'Substraction: {num1-num2}')
if num2 ==0:
    print("Divide: Impossible")
else:
    print(f"Divide: {num1/num2}")
'''

#[DONE]Bài 2:
#Viết chương trình lặp lại 10 số đầu tiên và trong mỗi lần lặp, in ra tổng của số hiện tại và số trước đó.
'''for i in range(9):
    print(i+(i+1))'''



#[done]Bài 3: Viết chương trình nhận một chuỗi từ người dùng và hiển thị các ký tự có ở số chỉ mục chẵn.
#Ví dụ: str = "pynative" thì bạn nên hiển thị ‘p’, ‘n’, ‘t’, ‘v’.
'''s=str(input("Input a string: "))
lst=list(s)
n=len(lst)
new_lst=[]
for i in range(n+1):
    if i%2==0:
        new_lst.append(lst[i])
print(new_lst)'''




#[done]Bài 4:
#Viết chương trình in dãy số sau bằng vòng lặp.
'''1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

row = int(input("Input the number of rows: "))
for i in range(1, row+1):
    for j in range(1,i+1):
        print(j, end=' ')
    print("")
'''

#[DONE]Bài 5: 
#Viết chương trình nhận một số từ người dùng và tính tổng tất cả các số từ 1 đến một số đã cho.
#Ví dụ: nếu người dùng nhập 10 thì đầu ra phải là 55 (1+2+3+4+5+6+7+8+9+10)
'''s=int(input("Input a number: "))
lst=[]
for i in range(s+1):
    lst.append(i)
print(sum(lst))'''



#[DONE] Bài 6: Viết chương trình in bảng nhân của một số cho trước
'''Ví dụ: num = 2 nên đầu ra phải là:
2
4
6
8
10
12
14
16
18
20

num=int(input("Input a number: "))
for i in range(11):
    print(i*num)'''


#Bài 7:
#Viết chương trình đếm tổng các chữ số của một số bằng vòng lặp while.
#Ví dụ: số là 75869, vì vậy đầu ra phải là 5.



#Bài 8: Viết chương trình sử dụng vòng lặp for để in dãy số đảo ngược sau:
#5 4 3 2 1 
#4 3 2 1 
#3 2 1 
#2 1 
#1




#Bai 8: Viết chương trình Hiển thị các số từ -10 đến -1 bằng vòng lặp for.



#Bài 9: Viết chương trình hiển thị tất cả các số nguyên tố trong một phạm vi (tự định nghĩa)



#Bài 10: Viết chương trình Hiển thị dãy Fibonacci lên đến 10 số hạng



#Bài 11: Viết chương trình Đảo ngược 1 số nguyên
#Given: 76542
#Expected output: 24567



#Bài 12: Viết chương trình in mẫu bắt đầu sau bằng vòng lặp for:
'''* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*'''

