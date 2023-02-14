a=[]
for i in range(1,6):
    for j in range(1,i+1):
        a.append(j)
b=a[::-1]
for k in range(len(b)):
    b[k]=str(b[k])
print(' '.join(b))