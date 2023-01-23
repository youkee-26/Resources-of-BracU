#task-01(b)
file2 = open('output1b.txt', 'w')
with open("input1b.txt","r") as file:
    list_first=file.readlines()
    list_second=[]
    for j in list_first:
        list_second.append(j.strip())
    no1=int(list_second[0])
    for k in range(1,no1+1,1):
        str1=list_second[k]
        s,n1,ope,n2=str1.split()
        if(ope=="+"):
            file2.write(f"The result of {n1} {ope} {n2} is {int(n1)+int(n2)}\n")
        elif(ope=="-"):
            file2.write(f"The result of {n1} {ope} {n2} is {int(n1)-int(n2)}\n")
        elif(ope=="*"):
            file2.write(f"The result of {n1} {ope} {n2} is {int(n1)*int(n2)}\n")
        else:
            file2.write(f"The result of {n1} {ope} {n2} is {int(n1)/int(n2)}\n")
file2.close()