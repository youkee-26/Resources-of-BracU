#task-03
def bubbleSort(arr):
    ans="sorted"
    for i in range(len(arr)-1): #tester loop
        if(arr[i]>arr[i+1]):
            ans="not sorted"
    if(ans=="not sorted"):
        for i in range(len(arr)-1):
            for j in range(len(arr)-i-1):
                if (arr[j] >arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
file2 = open('output3.txt', 'w')    
with open("input3.txt","r") as file:
    list_first=file.readlines()  
    list_second=[]
    for j in list_first:
        list_second.append(j.strip())
    num1=int(list_second[0])    
    f2=list_second[1].split() 
    f3=[]
    for idx in f2:
        f3.append(int(idx)) 
    arr= bubbleSort(f3)
    file2.write(f"Output\n")
    for idx in arr:
        file2.write(f"{str(idx)} ")
file2.close()
#In the loop which is termed as 'tester loop',it is checked at first whether the given array is already sorted(best case) or not. The loop will run on every element present in the array. 
#So it will run in θ(n) time complexity. If the array is already sorted then the nested for loop will not run. This is how I have achieved the θ(n) for the best-case scenario.