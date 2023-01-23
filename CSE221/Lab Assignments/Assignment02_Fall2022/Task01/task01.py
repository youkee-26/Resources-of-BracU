#task-01
file1 = open('output1.txt', 'w')
with open("input1.txt","r") as file:
    lines_list=file.readlines()
    n=int(lines_list[0])
    list_second=[]
    for j in   lines_list:
        list_second.append(j.strip())
    list_2=list_second[1].split()
    list_3=list_second[2].split()
    st_id=[]
    st_mk=[]
    for idx in list_2:
        st_id.append(int(idx))
    for idx in list_3:
        st_mk.append(int(idx))
    dict_1={}
    for idx in range(0,len(st_id)):
        if(st_mk[idx] not in dict_1):
            dict_1[st_mk[idx]]=[st_id[idx]]  
        else:
            dict_1[st_mk[idx]].append(st_id[idx])  #dict_1={50:452,40:111,20:343}
    for i in range(1,len(st_mk)):
         temp=st_mk[i]
         j=i-1
         while(j>=0 and st_mk[j]<temp):
             st_mk[j+1]=st_mk[j]
             j-=1
         st_mk[j+1]=temp
    print(st_mk)
    print(dict_1)
    for idx in st_mk:
        if(idx in dict_1):
         for idx_2 in dict_1[idx]:
            file1.write(str(idx_2)+" ")
         del dict_1[idx]
file1.close()    