try:
    with open('monhoc.txt', 'r', encoding='utf-8') as file_o:
        content = file_o.read()
        print(content)
except FileNotFoundError:
    print('File not found')
    file_o.close()