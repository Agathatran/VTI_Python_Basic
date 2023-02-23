class Student_and_grade():
    def __init__(self):
        pass
    def Student_info(self):
        print('Please choose one of the following functions')
        print('Add')
        print('Edit')
        print('Delete') 
        print('Search')
        str_input = str(input('I choose ')) 
        str_input = str_input.upper()
        if str_input == 'ADD':
            print('Please add the new information')
        elif str_input == 'EDIT':
            print('Please edit the information')
        elif str_input == 'DELETE':
            print('Choose the information that you want to delete')
        elif str_input == 'SEARCH':
            print('Input the student\'s name or student\' number')
    def Subject_info(self):
        print('Please choose one of the following functions')
        print('Add')
        print('Edit')
        print('Delete') 
        print('Search')
        str_input = str(input('I choose ')) 
        str_input = str_input.upper()
        if str_input == 'ADD':
            print('Please add the new information')
        elif str_input == 'EDIT':
            print('Please edit the information')
        elif str_input == 'DELETE':
            print('Choose the subject that you want to delete')
        elif str_input == 'SEARCH':
            print('Input the subject\'s name or subject\'s number')

