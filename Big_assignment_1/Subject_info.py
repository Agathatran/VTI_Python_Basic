def Subject_info():
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
Subject_info()