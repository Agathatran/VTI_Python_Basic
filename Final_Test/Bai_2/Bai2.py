input_str = str(input("Nhap vao chuoi ki tu: "))
str_list = input_str.split()
upper_list=[]
lower_list = []
other_list=[]
for i in input_str:
    if i.islower()==True:
        lower_list.append(i)  
    elif i.isupper()==True:
        upper_list.append(i)
    else:
        other_list.append(i)     
    upper_len = len(upper_list)
    lower_len = len(lower_list)
print(f"So ki tu thuong la: {lower_len}")   
print(f"So ki tu in hoa la: {upper_len}")

    
