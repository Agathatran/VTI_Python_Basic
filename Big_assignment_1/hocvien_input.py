def main():
    num_stu = int(input("How many students are there?"))
    with open ('hocvien.txt','w') as stu_input:
        for stu in range(1,num_stu+1):
            print(f"Input the information of student {stu}: ")
            stu_No = str(input("Student Number: "))
            name = str(input("Student's name: "))
            Date_birth = str(input("Date of birth: "))
            Place_birth = str(input("Place of birth: "))
            Phone = str(input("Phone number: "))
            mail = str(input("Email address: "))
            #Write the student's information as a record to the file:
            stu_input.write(stu_No + ' | ' + name + ' | ' + Date_birth +  ' | ' + Place_birth + ' | ' + Phone + ' | ' + mail + ' |' + '\n')
            print(f"Input student's information successfully!")

main() 
            