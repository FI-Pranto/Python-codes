s=input()
res=""
sub=""
n=len(s)
for i in range(n+1):
    if i==n or s[i]==" ":
        res=res+sub+" "
        sub=""
    else:
        sub=s[i]+sub
        
print(res)        
        