#[DONE]Bài 1: Đảo ngược một list trong Python: Ví dụ: 100, 200, 300, 400, 500] --> [500, 400, 300, 200, 100]
#How to input a list?
'''str=str(input("Input a list: "))
lst=list(str)
print("The inputted list is: ", lst)
rev_lst=lst[::-1]
print(rev_lst)
#Dap An
list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)'''
#Question: trong bài tự mình input mà dùng .reverse() thì kết quả lại ra là none???


#[Chua xong]Bài 2: Viết chương trình cộng hai danh sách (các phần tử kiểu string) theo index. Tạo một danh sách mới bằng cách cộng các phần từ tại vị trí tương ứng của 2 danh sách với nhau.
#Ví dụ: list1 = ["M", "na", "i", "Ke"] 
# list2 = ["y", "me", "s", "lly"]
#--> ['My', 'name', 'is', 'Kelly']
'''str1=str(input("Input the first string: "))
lst1=str1.split(" ")
print("The first string is",lst1)
str2=str(input("Input the second string: "))
lst2=str2.split(" ")
newlst=[]
print("The second string is: ", lst2)
if len(lst1)!=len(lst2):
    print("Impossible")
else:
    for i in range(len(lst1)):
        newlst.append(lst1[i])
        newlst.append(lst2[i])
        newstr=' '.join(newlst)
        print(newstr)'''
#Dap an
'''list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)'''
#Question: giải thích về lệnh zip(list1, list2)


#[Correct]Bài 3: Cho một danh sách các số. Tạo danh sách mới bằng cách bình phương mỗi phần tử của danh sách đó. Ví dụ: numbers = [1, 2, 3, 4, 5, 6, 7] --> [1, 4, 9, 16, 25, 36, 49]
'''str=str(input("Input the list of number: "))
lst=str.split(' ')
sqrt_lst=[]
print("The input string is: ", lst)
for i in range(0,len(lst)):
    lst[i]=int(lst[i])
    print("The inputted list is:", lst)
    sqrt_lst.append(lst[i]**2)
    print("The list of taken square numbers is: ", sqrt_lst)'''

'''# Solution 1: Using loop and list method
numbers = [1, 2, 3, 4, 5, 6, 7]
# result list
res = []
for i in numbers:
    # calculate square and add to the result list
    res.append(i * i)
print(res)

# Solution 2: Use list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7]
res = [x * x for x in numbers]
print(res)'''


#[DONE]Bài 4: Cho 2 danh sách. Viết chương trình lặp đồng thời cả hai danh sách và hiển thị các phần tử của danh sách 1 theo thứ tự ban đầu và các phần tử của danh sách 2 theo thứ tự ngược lại.
#Ví dụ: list1 = [10, 20, 30, 40] list2 = [100, 200, 300, 400] --> 10 400 20 300 30 200 40 100
#Raise: Nếu nhập nhầm 1 kí tự là chữ thì cần phải báo lỗi
#Input 2 lists
'''
Arg:
str1, str2 (str): Input string
lst1,lst2 (list): Input list
newlst: the list combined by lst1 and the reverse of lst2
'''
'''str1=str(input("Input the first list: "))
lst1 = str1.split(' ')
str2=str(input("Input the second list: "))
lst2=str2.split(' ')
newlst=[]
for i in range(0,len(lst1)):
#Check whether input list entries are all numbers
    if (lst1[i].isnumeric()==False):
        print("Input incorrectly")
        break;
    else:
        print("The first list is: ",lst1)
        lst1[i]=int(lst1[i])
        newlst.append(lst1[i])
for j in range(0,len(lst2)):
    if (lst2[i].isnumeric()==False):
        print("The second list is input incorrectly")
        break;
#Reverse list 2 and add to the new list
    else:
        revlst2=lst2[::-1]
        lst2[j]=int(lst2[j])
        newlst.append(lst2[j])
    print(newlst)'''

#Solution --->#Solution không chạy

'''list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for x, y in zip(list1, list2.reverse()):
    print(x, y)'''

#[Not done] Bài 5: Xóa các chuỗi rỗng khỏi danh sách các chuỗi Ví dụ: list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"] --> ["Mike", "Emma", "Kelly", "Brad"]
#filter(None, list1) ---> khi dùng lệnh này kết quả trả ra là dạng gì?
'''list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
for i in range(0,len(list1)):
    if (list1[i]=='\"\"'):
        list1.pop()
        print(list1)'''
#Solution
'''list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# remove None from list1 and convert result into list
res = list(filter(None, list1))

print(res)'''





#[Correct] Bài 6: Viết chương trình thêm sô 7000 vào sau số 6000 trong Danh sách sau: list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40] --> [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
'''list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1) 
'''



#Bài 7[Correct]: Cho một danh sách lồng nhau. list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
#Viết chương trình mở rộng nó bằng cách thêm danh sách con ["h", "i", "j"] sao cho nó giống như danh sách sau. ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
'''list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list2=["h", "i", "j"]
list1[2][1][2].extend(list2)
print(list1)
'''


#[DONE]Bài 8: Viết chương trình tìm giá trị 20 trong danh sách, nếu có thì thay bằng 200. 
# Chỉ cập nhật lần xuất hiện đầu tiên của no. Ví dụ: list1 = [5, 10, 15, 20, 25, 50, 20] --> [5, 10, 15, 200, 25, 50, 20]

###Làm sai
'''str=str(input("Input the string: "))
lst=str.split(" ")
for i in range(0,len(lst)):
    lst[i]=int(lst[i])
    if lst[i]==20:
        lst[i]=200
        print(lst)'''
#Solution
'''list1 = [5, 10, 15, 20, 25, 50, 20]
# get the first occurrence index
index = list1.index(20)
# update item present at location
list1[index] = 200
print(list1)'''

#other
'''
idx_20=0
for idx,val in enumerate(list1):
    if val==20:
        break
list1[idx_20]==200
'''
#other
'''idx_20=0
i=0
for val in list1:
    i+=1
    if val ==20:
        idx_20==i 
        break
list1[idx_20]==200'''

#[DONE]Bài 9: Viết chương trình loại bỏ tất cả các lần xuất hiện của số 20 trong list: 
# Ví dụ: list1 = [5, 20, 15, 20, 25, 50, 20] --> [5, 15, 25, 50]

'''str=str(input("Input the string: "))
lst=str.split(" ")
for i in range(0,len(lst)):
    if lst[i].isnumeric()==False:
        print("Input incorrectly")
    else:
        lst[i]=int(lst[i])
        if lst[i]==20:
            lst.pop()
        print(lst)'''
#Solution
'''
def remove_value(sample_list, val):
    return [i for i in sample_list if i != val]
res = remove_value(list1, 20)
print(res)

# Solution 2: while loop (slow solution)
list1 = [5, 20, 15, 20, 25, 50, 20]

while 20 in list1:
    list1.remove(20)
print(list1)'''