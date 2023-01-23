file1 = open('output1a.txt', 'w')
with open("input1a.txt","r") as file:
    lines_list=file.readlines()
    list_2=[]
    for i in lines_list:
        list_2.append(i.strip())
    num1=int(list_2[0])
    for idx in range(1,num1+1,1):
      if (int(list_2[idx])%2==0):
        file1.write(f"{list_2[idx]}, the number is even.\n")
      else:
        file1.write(f"{list_2[idx]}, the number is odd.\n")
file1.close()