list=[1,2,5,9,102,101,3,4]

maxi=list[0]

i=1
length=len(list)
while i<length:
    if maxi<list[i]:
        maxi=list[i]
    
    i=i+1

print(maxi)        

  

    