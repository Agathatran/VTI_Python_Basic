def Grading_Scheme():
    print('Please choose one of the following functions')
    print('Input grade')
    print('Edit Grade')
    print('Delete Grade') 
    print('Search')
    print('Summary of results')
    str_input = str(input('I choose ')) 
    str_input = str_input.upper()
    if str_input == 'INPUT GRADE':
        print('Please add the new information')
    elif str_input == 'EDIT GRADE':
        print('Please edit the information')
    elif str_input == 'DELETE GRADE':
        print('Choose the grade that you want to delete')
    elif str_input == 'SEARCH':
        sub_input = str(input('Input the subject number or subject name'))
    elif str_in == "SUMMARY OF RESULTS":
        print('Here is the result.')
Grading_Scheme()