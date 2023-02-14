#[DONE]Bài 1: Viết chương trình tạo một chuỗi mới gồm ký tự đầu tiên, giữa và cuối cùng của chuỗi đầu vào. Ví du: "James" --> "Jms"
word=str(input('Input word'))
n=len(word)
k=n%2
if k == 0:
    print(word[0]+word[n//2-1]+word[-1])
else:
        print(word[0]+word[n//2]+word[-1])
#[DONE]Bài 2: Cho hai chuỗi s1 và s2. Viết chương trình tạo một chuỗi mới s3 bằng cách thêm s2 vào giữa s1. Ví du: s1 = "Ault" s2 = "Kelly" --> AuKellylt
s1=str(input("Input the 1st string: "))
s2= str(input("Input the 2nd string: "))
n=len(s1)
k=n//2
print(s1[:k] + s2 + s1[k:])
                    
# DONE Bài 3: Chuỗi đã cho chứa tổ hợp chữ thường và chữ hoa. Viết chương trình sắp xếp các ký tự của một chuỗi sao cho tất cả các chữ cái viết thường sẽ xuất hiện trước.
#  Ví du: 'PyNaTive' --> 'yaivePNT'
s=str(input("Input a string: "))
char_upper=[]
char_lower=[]
char_other=[]
for i in s:
    if i.islower()== True:
        char_lower.append(i)
    elif i.isupper()== True:
        char_upper.append(i)
print(''.join(char_lower + char_upper))

#[DONE] Bài 4: Đếm tất cả các chữ cái, chữ số và ký hiệu đặc biệt từ một chuỗi đã cho. Ví dụ: "P@#yn26at^&i5ve" 
# -->#Total counts of chars, digits, and symbols Chars = 8 Digits = 3 Symbol = 4
s= str(input("Input a string: "))
Cha=[]
Sym=[]
Dig=[]
for i in s:
    if (i.islower()==True or i.isupper()==True):
        Cha.append(i)
    elif i.isnumeric()== True:
        Dig.append(i)
    else:
        Sym.append(i)
print(dict([('Cha', len(Cha)),('Sym', len(Sym)), ('Dig', len(Dig))]))
#[DONE] Bài 5: Viết chương trình tìm tất cả các lần xuất hiện của “USA” trong một chuỗi đã cho, bỏ qua trường hợp này. 
# Ví du: "Welcome to USA. usa awesome, isn't it?" --> The USA count is: 2
s=str(input("Input a string: "))
s_upper=s.upper()
sub_string='USA'
# convert string to lowercase

# use count function
count = s_upper.count(sub_string)
print("The USA count is:", count)


#[DONE]Bài 6: Cho một chuỗi s1, hãy viết chương trình trả về tổng và trung bình cộng của các chữ số xuất hiện trong chuỗi, bỏ qua tất cả các ký tự khác. Ví dụ: str1 = "PYnative29@#8496" --> Sum is: 38 Average is 6.333333333333333
s=str(input("Input a string:"))
lst=[]
for i in s:
    if i.isnumeric()==True:
        lst.append(i)
        number=[int(m) for m in lst]
        ave= sum(number)/len(lst)
print(ave)       

# DONE Bài 7: Viết chương trình đếm số lần xuất hiện của tất cả các ký tự trong một chuỗi Ví duj: str1 = "Apple" --> {'A': 1, 'p': 2, 'l': 1, 'e': 1}
s=str(input("Input a string"))
draft={}
for i in s:
    if i in draft:
        draft[i]+=1
    else:
        draft[i]=1
print("The result is \n",str(draft))
#Bài 8: Viết chương trình tìm vị trí cuối cùng của chuỗi con “Emma” trong một chuỗi đã cho. 
# "Emma is a data scientist who knows Python. Emma works at google."


#[DONE]Bài 9: Viết chương trình tách một chuỗi đã cho trên dấu gạch nối và hiển thị từng chuỗi con. Ví dụ: str1 = Emma-is-a-data-scientist 
# #Emma is a data scientist-->
s1=str(input("Nhap mot chuoi: "))
s2=s1.split('-')
for i in s2:
    print(i)
#[DONE]Bài 10: Xóa các ký hiệu/dấu chấm câu đặc biệt khỏi chuỗi Ví du: str1 = "/*Jon is @developer & musician" --> "Jon is developer musician"
s=str(input("Input a string: "))
new=[]
for i in s:
    if ((i.islower()==True) or (i.isupper()==True) or (i.isnumeric()==True)):
        new.append(i)
print(''.join(new))

    