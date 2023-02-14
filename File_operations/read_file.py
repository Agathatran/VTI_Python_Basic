value_config=[]
try:
    with open('text1.txt','r',encoding='utf-8') as file_o:
        content=file_o.readlines()
        for line in content:
            value=line.split(':')[1].strip()
            print(value)
except FileNotFoundError:
    print("File not found")
    file_o.close()
