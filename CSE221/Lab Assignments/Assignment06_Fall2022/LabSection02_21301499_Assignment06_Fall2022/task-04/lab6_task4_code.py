#task-04
file1 = open('task4_output.txt', 'w')
with open("task4_input.txt","r") as file:
  lines_list=file.readlines()
  lines_list=lines_list[:len(lines_list)-1]
  list_second=[]
  for j in   lines_list:
        list_second.append(j.strip())
  for idx in range(0,len(list_second)):
      lines=list_second[idx].split()
      st=int(lines[0])
      end=int(lines[1])
      sq=0
      for idx_2 in range(st,end+1):
          x=str(idx_2**(1/2))
          if(x[len(x)-2:len(x)]==".0"):
              sq+=1
      file1.write(str(sq)+"\n")
file1.close()