#TAKING SPACE GENERATED INPUTS
n=int(input("Enter the number of games played: "))
lst=list()
arr=[int(num) for num in input().split()]
#print(arr)
for i in range(n):
    lst.append(arr[i])
#print(lst)
min1=max1=lst[0]
#print(min1,max1)
max1_cnt=min1_cnt=0
for i in range(n):
    if(lst[i]>max1):
        #print(max1,lst[i])
        max1=lst[i]        
        #print("\n")
        #print("The new max is: "+str(max1))
        max1_cnt=max1_cnt+1
    elif(lst[i]<min1):
        min1=lst[i]
        min1_cnt=min1_cnt+1
    
print(max1_cnt,min1_cnt)
