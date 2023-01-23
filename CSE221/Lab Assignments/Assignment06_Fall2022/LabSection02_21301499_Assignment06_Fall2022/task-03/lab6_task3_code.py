#task-03
file1 = open('task3_output.txt', 'w')
with open("task3_input.txt","r") as file:
  lines_list=file.readlines()
  list_second=[]
  for j in   lines_list:
        list_second.append(j.strip())
  total_task=list_second[0]
  lines=list_second[1].split(" ")
  list_task=[]
  for j in   range(0,len(lines)):
        list_task.append(int(lines[j]))
  names=list_second[2]
  jack=0
  j=[]
  jill=0
  list_task.sort()
  count=0
  str1=""
  for nm in names:
      if(nm=='J'):
         str1+=str(list_task[count])
         jack+=list_task[count]
         j.append(list_task[count])
         count+=1
      else:
          u=j.pop(-1) #stack implementation 
          str1+=str(u)
          jill+=u
  file1.write(f"{str1}\nJack will work for {jack} hours\nJill will work for {jill} hours")
file1.close()