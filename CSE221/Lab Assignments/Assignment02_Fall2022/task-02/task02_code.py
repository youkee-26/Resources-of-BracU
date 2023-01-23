#task-02(ii)
file2 = open('output2.txt', 'w')
with open("input2.txt","r") as file:
    lines_list=file.readlines()
    list_second=[]
    for j in   lines_list:
        list_second.append(j.strip())
    n=list_second[0]
    ele=list_second[1].split()
    list_2=[]
    for i in ele:
        list_2.append(int(i))
    #merge sort alogorithm
    def merge(a1, a2):
      left = 0 
      right = 0 
      final_sort = 0
      final = [0] *(len(a1)+ len(a2))
      while (left<len(a1) and right<len(a2)):
        if (a1[left]<a2[right]):
          final[final_sort] = a1[left]
          left += 1
          final_sort += 1
        else :
          final[final_sort] = a2[right]
          right+= 1
          final_sort += 1
      if (left<len(a1)):
        idx = left
        for i in range (idx,len(a1)):
          final[final_sort] = a1[i]
          final_sort += 1
      if (right<len(a2)):
        idx = right
        for right in range (idx,len(a2)):
          final[final_sort] = a2[right]
          final_sort += 1
      return final
    def merge_sort(arr):
      if len(arr) <= 1:
        return arr
      else :
        mid=len(arr)//2
        a1 = merge_sort(arr[0:mid])
        a2 = merge_sort(arr[mid:len(arr)])
        return merge(a1, a2)
    arr=list_2
    met=merge_sort(arr)
    for idx in met:
        file2.write(str(idx)+" ")
file2.close()