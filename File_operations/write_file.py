'''
1. Open file
2. Write file
3. Close
'''

'''#Method 1:
file_w=open('text1.txt', 'w', encoding='utf-8')
file_w.write('2. Write file')
file_w.close'''

'''#Method 2:
try:
    with open('text1.txt','w', encoding='utf-8') as   file_w:
        file_w.write('')
except:
    print('Error')'''

lines=["line1 \n", "line2"]
with open('text1.txt','w', encoding='utf-8') as   file_w:
        file_w.writelines(lines)