def main():
    num_grade = int(input("How many subjects are there?"))
    with open ('diemthi.txt','w') as grade_input:
        for grade in range(1, num_grade+1):
            print(f"Input the information of student {grade}: ")
            stu_no = str(input("Student Number: "))
            stu_name = str(input("Student's name: "))
            sub_code = str(input("Input subject code: "))
            sub_name = str(input("Input subject name: "))
            attendance = str(input("Attendance grade: "))
            midterm= str(input("Midterm grade: "))
            final = str(input("Final Grade: "))
            #Write the student's information as a record to the file:
            grade_input.write(stu_no + ' | ' + stu_name + ' | ' + sub_code + '|' + sub_name + '|' + attendance +  ' | ' + midterm + ' | ' + final + '\n')
            print(f"Input grade successfully!")

main() 