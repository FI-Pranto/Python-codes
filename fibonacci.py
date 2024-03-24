n=int(input())
t1=0
t2=1
print(t1)
print(t2)
for i in range(2,n):
    sum=t1+t2
    t1=t2
    t2=sum
    print(t2)
    
