it=1
t=int(input())
while it<=t :
    n=int(input())
    s=input()
    s=s.split(" ")
    list=[int(i) for i in s]
    if list.count(0)>1:
        print("0")
    else:
         mini=min(list)
         mul=1
         for x in list:
            if x==0:
               continue
            else:
               mul=mul*x
               time=0

         if mini!=0:    
             mul=int(mul/mini)
         mul=mul*(mini+1)
         print(mul)
    it+=1

   