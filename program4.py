n=int(input("Enter the number of integers:"))
list=[]
for i in range(0,n):
    num=int(input("Enter the value:"))
    if(num>100):
        list.append("Over")
    else:
        list.append(num)
print(list)