dict={}

s="hello how are you"
for i in s:
    if i not in dict:
         dict[i]=1
    else:
        dict[i]+=1
stack=""        
for i in s:
    if i not in stack:
       print(i,dict[i])
       stack+=i  
          


