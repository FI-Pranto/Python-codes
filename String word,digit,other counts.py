s=input()
wc=dc=oc=0
for x in s:
    if x >="A" and x<="z":
        wc+=1
    elif x>="0" and x<="9":
        dc+=1
    else:
        oc+=1

ans="""Word Count : {}
Digit Count : {}
Other Count : {}"""
print(ans.format(wc,dc,oc))      
        
        