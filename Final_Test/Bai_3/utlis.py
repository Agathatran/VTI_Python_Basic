def read_txt_file(file_path): 
    with open(file_path, 'r', encoding = 'utf-8') as file_o:
        content = file_o.readlines()
        return content


def write_txt_file(file_path, contents, mode = 'a'):
    with open(file_path, mode, encoding ='utf-8') as file_rw:
        # currrent_content = file_rw.readlines()
        
        file_rw.writelines( [contents[0]+"\n"] )
        return True



