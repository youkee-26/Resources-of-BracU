file2 = open('output5.txt', 'w')    
with open("input5.txt","r") as file:
    list_first=file.readlines()  
    list_second=[]
    for j in list_first:
        list_second.append(j.strip())
    num1=int(list_second[0])
    alpha=[]
    loc=[]
    time=[] 
    temp=[]
    dict_1={}
    for i in range(1,num1+1,1):
        list_1=list_second[i].split()
        alpha.append(list_1[0])
        loc.append(list_1[4])
        temp.append(list_1[6])
    for j in temp:
        y=j.split(":")
        time.append(int(y[0]+y[1]))
    for idx in range(0,len(alpha)):
        if(alpha[idx] not in dict_1.keys()):
            dict_1[alpha[idx]]=[[loc[idx],time[idx]]]  #{"ABCD":[["Mymen",30],["Chittagong ",100]]}
        else:
            dict_1[alpha[idx]].append([loc[idx],time[idx]])   
    #dict_1 ={'ABCD': [['Mymensingh', 30], ['Chittagong', 100]], 'DhumketuExpress': [['Chittagong', 230]]}
    for key in dict_1.keys():
        list_f=dict_1[key] #list_f=[['Mymensingh', 30], ['Chittagong', 100]]
        #sorting(selection sort) the timing
        for idx_2 in range(len(list_f)):
            min_idx=idx_2
            for j in range(idx_2+1,len(list_f),1):
                if(list_f[j][1]>list_f[min_idx][1]):
                    min_idx=j
            tempp=list_f[idx_2]
            list_f[idx_2]=list_f[min_idx]
            list_f[min_idx]=tempp
#print(dict_1)
    for idx in range(0,len(alpha)):
        for idx_2 in range(len(alpha)):
            min_idx=idx_2
            for j in range(idx_2+1,len(alpha),1):
                if(alpha[j]<alpha[min_idx]):
                    min_idx=j
            tempp=alpha[idx_2]
            alpha[idx_2]=alpha[min_idx]
            alpha[min_idx]=tempp
    for key in alpha:
      if(key in dict_1.keys()):
        list_f=dict_1[key]
        for j in list_f:
            tym_2=j[1]
            if(len(str(tym_2))==1):
                str1="00:0"+str(tym_2)
            elif(len(str(tym_2))==2):
                str1="00:"+str(tym_2)
            elif(len(str(tym_2))==3):
                str1="0"+str(tym_2)[0]+":"+str(tym_2)[1:]
            else:  
                str1=str(tym_2)[0:2]+":"+str(tym_2)[2:]    
            file2.write(f"{key} will departure for {j[0]} at {str1}\n")
        del dict_1[key]
file2.close()