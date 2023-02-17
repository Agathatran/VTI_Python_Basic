# This program gets employee data from the user and saves it as records in the employee.txt file
'''def write_emp_info():
    num_emps = int(input('How many employees records to create? '))
    #open file employee.txt for writing
    with open('employee.txt','w') as emp_file:
        for emp in range(1,num_emps +1):
            #get data of number emp
            print(f'Enter information for emplyee {emp}: ')
            name = input('Name: ')
            id_num = input('ID number: ')
            dept = input('Department: ')

            #write the employee;'s information as a record to the file:
            emp_file.write(name + '\n')
            emp_file.write(id_num + '\n')
            emp_file.write(dept + '\n')
            # print seperate line between users
            print('--------------------------------------------')
        print(f'All employee information are saved!')
#call the main function
# Method 1: main()
#Method 2:'''
'''if __name__ == '__main__':
    main()'''


def red_emp_info():
    #open file
    with open('employee.txt','r') as emp_file:
        for ind, line in enumerate(emp_file.readlines()):
            if ind ==0:
                continue
            print(f'Information of employee {ind+1}')
            name = line.split("\t")[0]
            print(f'Name: {name}')
            id_num = line.split("\t")[1]
            print(f'ID Number: {id_num}')
            depart= line.split("\t")[2]
            print(f'Department: {depart}')
            print('-----------------------')
red_emp_info()

    