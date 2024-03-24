'''input_num=input()
rev_num=input_num[::-1]
rev_num=int(rev_num)
input_num=int(input_num)

if rev_num==input_num:
    print("Plaindrom")
else:
    print("Not Plaindrom") '''

for i in range(1,6):
    s=""
    for j in range(0,6-i-1):
        s=s+" "
    for k in range(0,i):
        s=s+"*"
    print(s)   
      
for i in range(1,6):
    s=""
    for j in range(0,i):
        s=s+" "
    for k in range(0,6-i-1):
        s=s+"*"
    print(s)    
          


    