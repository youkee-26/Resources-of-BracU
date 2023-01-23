#task-04(heap sort)
file4 = open('output4b.txt', 'w')
with open("input4.txt","r") as file:
    lines_list=file.readlines()
    list_second=[]
    for j in   lines_list:
        list_second.append(j.strip())
    dict_1={}
    list_ser=[]
    #list_second=['ABC 3', 'EWQ 3', 'SDF 2']
    def heapify(list_ser,num1,nodes):
      max=nodes
      starting=(2*nodes)+1
      ending=(2*nodes)+2 
      if(starting<num1 and list_ser[max]<list_ser[starting]):
          max=1
      if (ending<num1 and list_ser[max]<list_ser[ending]):
          max=ending
      if (max!= nodes):
          list_ser[nodes],list_ser[max]=list_ser[max],list_ser[nodes]
          heapify(list_ser,num1,max) 
    def heapSort(list_ser):
        num1=len(list_ser)
        for idx in range(num1//2-1,-1,-1):
            heapify(list_ser,num1,idx)
        for idx_2 in range(num1-1,0,-1):
            list_ser[0],list_ser[idx_2]=list_ser[idx_2],list_ser[0]
            heapify(list_ser,idx_2,0)
    def enque(list_ser,dict_1):
        arr=[0]*20
        front=0
        capacity=len(arr)-1
        list_con=[]
        if(capacity==0):
            print("The Queue is full")
        else:
         for ser in list_ser:
            if(ser not in list_con):
               for names in dict_1[ser]: 
                   arr[front]=names 
                   front+=1
                   capacity-=1
               list_con.append(ser)
        return arr   
    def printQueue():
        str4=""
        for i in arr:
            if(i!=0):
                str4+=i+", "
        file4.write(f"Remaining patients: {str4[:len(str4)-2]}\n")
    def seeDoctor(arr,list_ser): #dequque method
        for j in range(0,len(arr),1):
            i=j
            if(arr[i]!=0):
                file4.write(arr[i]+"\n") 
                for key in dict_1.keys():#dict_keys([3, 2, 1])
                    if(arr[i] in dict_1[key]):
                        d=key
                        break
                if(len(dict_1[d])==1):
                    del dict_1[d]
                    list_4=[]
                    for element in list_ser:
                        if(element!=d):
                            list_4.append(element)
                    list_ser=list_4
                else:
                    list_3=dict_1[d][1:]
                    dict_1[d]=list_3
                arr[i]=0
                printQueue()
                break
        return list_ser
    for idx in range(0,len(list_second),1):#list_second=['ABC 3', 'EWQ 3', 'SDF 2']
        if(list_second[idx]!="see doctor" and list_second[idx]!="print"):
            name,x=list_second[idx].split()
            ser=int(x)
            list_ser.append(ser) #list_ser=[1,2,3,3]
            if(ser not in dict_1): #dict_1={3: ['ABC', 'EWQ'], 2: ['SDF'], 1: ['KLM']}
                dict_1[ser]=[name]
            else:
                dict_1[ser].append(name)
            heapSort(list_ser)
            arr=enque(list_ser,dict_1)
        elif(list_second[idx]=="print"):
            printQueue()
        else:  
            list_ser=seeDoctor(arr,list_ser)
file4.close()
