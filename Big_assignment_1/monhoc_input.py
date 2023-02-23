def main():
    num_sub = int(input("How many subjects are there?"))
    with open ('monhoc.txt','w') as stu_input:
        for sub_info in range(1,num_sub+1):
            print(f"Input the information of subjects {sub_info}: ")
            sub_code = str(input("Subject Code: "))
            sub_name = str(input("Subject's name: "))
            #Write the student's information as a record to the file:
            stu_input.write(sub_code + ' | ' + sub_name + '\n')
            print(f"Input subjects' information successfully!")

main() 