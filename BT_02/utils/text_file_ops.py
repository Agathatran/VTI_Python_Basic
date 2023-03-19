def read_txt_file(file_path):
    # try:
    with open(file_path, 'r+', encoding='utf-8') as file_o:
        content = file_o.readlines()
    # except FileNotFoundError:
    #     print('File not found')
    #     file_o.close()
    return content

def write_txt_file(file_path, contents, mode):
    # try:
    with open(file_path, mode, encoding='utf-8') as file_rw:
        # read content
        current_content = file_rw.readlines()
        # print(current_content)
        # write content
        file_rw.writelines(contents)
        return True
    # except:
    #     print('Error writing file')
    #     return False