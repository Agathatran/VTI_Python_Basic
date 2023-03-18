def read_txt_file(file_path): #ham doc file
    with open(file_path, 'r', encoding = 'utf-8') as file_o:
        content = file_o.readlines()
        return content

    #         for line in content:
    #             value = line.split(':')[1].strip()
    #             value_config.append(Value)
    # except FileNotFoundError:
    #     print("File is not founded.")
    #     file.closed()
    # return value_config

def write_txt_file(file_path, contents, mode):
    #try:
    with open(file_path, mode, encoding ='utf-8') as file_rw:
        currrent_content = file_rw.readlines()
        # print(current_content)
        # file_rw.writelines(contents)
        file_rw.writelines(contents)
        return True
    # except:
    #     print('Error writing file')
    #     return False


