#3(ii)
file3 = open('output3b.txt', 'w')
with open("input3b.txt","r") as file:
    lines_list=file.readlines()
    list_second=[]
    def partition(arr,st,end):
        j=st-1  
        pivot= arr[end]
        idx_3=st
        while(idx_3<end):
            if(arr[idx_3]<=pivot):   
                j+=1
                arr[idx_3],arr[j]=arr[j],arr[idx_3]
            idx_3+=1
        arr[end],arr[j+1]=arr[j+1],arr[end]
        return j+1
    def findk(arr,k,st,end):
      if (st<=end):
        temp=partition(arr,st,end)
        if (temp<k):
          return findk(arr,k,temp+1,end)
        elif (temp>k):
          return findk(arr,k,st,temp-1)
        else:
            return arr[temp]  
      
    for j in   lines_list[1:]:
        list_second.append(j.strip())
    for ele in range(0,len(list_second[0]),1): #list_second[0]='The array: 1 3 4 5 9 10 10'
        if(48<=ord(list_second[0][ele])<=57):
            ans=ele
            break
    list_str=list_second[0][ele:].split()
    arr=[]
    for i in list_str:
        arr.append(int(i))
    for idx in list_second[1:len(list_second)]:
       for idx_2 in idx:#idx=element
           if(48<=ord(idx_2)<=57):
               num=int(idx_2)
               index=findk(arr,num-1,0,len(arr)-1)
               file3.write(str(index)+"\n")
file3.close()   