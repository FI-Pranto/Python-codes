'''input_num=input()
rev_num=input_num[::-1]
rev_num=int(rev_num)
input_num=int(input_num)

if rev_num==input_num:
    print("Plaindrom")
else:
    print("Not Plaindrom") '''
def isPrime(n):
    if n==1 or n==0:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
    return True       
    

c=1
num=1
sum=0
while c<=100:
    if isPrime(num):
       # print(num)
        sum=sum+num
        c+=1
    num+=1    
print(sum)    

    
          


    