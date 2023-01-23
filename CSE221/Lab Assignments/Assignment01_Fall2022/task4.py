#task-04
file2 = open('output4.txt', 'w')
with open("input4.txt","r") as file:
    lines_list=file.readlines()
    list_second=[]
    stu_id=[]
    stu_marks=[]
    dict_1={}
    for j in   lines_list:
        list_second.append(j.strip())
    num1=int(lines_list[0])
    f1=lines_list[1].split()
    f2=lines_list[2].split()
    for idx in f1:
         stu_id.append(int(idx))
    for idx in f2:
         stu_marks.append(int(idx))
    for idx in range(num1):
        if(stu_marks[idx] not in dict_1.keys()):
            dict_1[stu_marks[idx]]=[stu_id[idx]]
        else:
            dict_1[stu_marks[idx]].append(stu_id[idx])
    #sorting(selection sort) the the student ids in the dictionary
    for idx in dict_1:
        for i in range(0,len(dict_1[idx]),1):
            min_idx=i
            for j in range(i+1,len(dict_1[idx]),1):
                if(dict_1[idx][j]<dict_1[idx][min_idx]):
                    min_idx=j
            temp=dict_1[idx][i]
            dict_1[idx][i]=dict_1[idx][min_idx]
            dict_1[idx][min_idx]=temp    
    #sorting(selection sort) the array in which marks are saved
    for i in range(0,num1,1):
        min_idx=i
        for j in range(i+1,num1,1):
            if(stu_marks[j]>stu_marks[min_idx]):
                min_idx=j
        temp=stu_marks[i]
        stu_marks[i]=stu_marks[min_idx]
        stu_marks[min_idx]=temp
    #printing the required output
    file2.write(f"Output:\n")
    for marks in stu_marks:
        if(marks in dict_1.keys()):
            for id in dict_1[marks]:
                file2.write(f"ID: {id} Mark: {marks}\n")
            del dict_1[marks]
file2.close()