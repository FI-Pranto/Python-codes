#the best way to declare list
#and take input in phython
n=3
num=[]

start = 1

while start < n:
        num.append(int(input()))
        num.append(input())
        start += 1

   
#phython list can contain int with string
#float and other type variable also
#This is the best way to declare list
#and take input in phython  

print(num)  # 👉️ [1, 2, 3, 4, 5]
#print(get_range(7))  # 👉️ [1, 2, 3, 4, 5, 6]
print(num[0]+num[2])
print(num[1]+num[3])  