file1 = open('output2.txt', 'w')
with open("input2.txt","r") as file:
  lines_list=file.readlines()
  list_second=[]
  for j in   lines_list:
        list_second.append(j.strip())
  lines=list_second[0].split()
  total=int(lines[0])
  total_p=int(lines[1])
  dict_1={}
  list_end=[]
  list_final=[]
  for idx in range(1,total+1):
      x=list_second[idx].split()
      st=int(x[0])
      end= int(x[1])
      list_end.append(end)
      list_final.append((st,end))
      if end not in dict_1:
          dict_1[end]=[st]
      else:
          dict_1[end].append(st) 
  list_end.sort()  
  #dict_1={4: [0, 3], 5: [1], 10: [9], 9: [6], 3: [2], 2: [1]}
  #list_end=[2, 3, 4, 4, 5, 9, 10]
  #list_final=[(0, 4), (3, 4), (1, 5), (9, 10), (6, 9), (2, 3), (1, 2)]
  list_final2=[]
  for idx in list_end:
      if(idx in dict_1):
          for indi in dict_1[idx]: #dict_1[idx]=   [0, 3] 
              list_final2.append((indi,idx))
  ans=[]
  while(total_p!=0):
    for idx_3 in range(0,len(list_final2)):
        if(idx_3==0):
            ans.append(list_final2[idx_3])
            y=list_final2[idx_3][1]
        else:
            if(list_final2[idx_3][0]==y or list_final2[idx_3][0]>y ):
                if(list_final2[idx_3] not in ans):
                  ans.append(list_final2[idx_3])
                  y=list_final2[idx_3][1]
    total_p-=1
  file1.write(str(len(ans)))
file1.close()