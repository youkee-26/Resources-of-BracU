#task-03(i)
file3 = open('output3a.txt', 'w')
with open("input3a.txt","r") as file:
    lines_list=file.readlines()
    list_second=[]
    for j in   lines_list:
        list_second.append(j.strip())
    n=list_second[0]
    ele=list_second[1].split()
    list_2=[]
    for i in ele:
        list_2.append(int(i))
    #quick_sort
    def quicksort(arr,st,end):
      if (st<end):
          mid= partition(arr,st,end)
          quicksort(arr,st,mid-1)
          quicksort(arr,mid+1,end)
    def partition(arr,st,end):
        i= st
        j= end-1
        pivot= arr[end]
        while(i<j):
            while(i<end and arr[i]<pivot):    
                i+=1
            while(j>st and arr[j]>=pivot):
                j-=1
            if(i<j):
                arr[i], arr[j]= arr[j], arr[i]
        if(arr[i]>pivot):
            arr[i], arr[end]= arr[end], arr[i]
        return i  #returns the index of pivot
    arr =list_2
    quicksort(arr, 0, len(arr)-1)
    for idx in arr:
        file3.write(str(idx)+" ")
file3.close()
