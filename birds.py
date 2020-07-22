n=int(input("Enter the number of birds: "))
lst=list()
arr=[int(num) for num in input().split()]
for i in range(n):
    lst.append(arr[i])
lst=sorted(lst)
#print(lst)
counts=dict()
for num in lst:
    counts[num]=counts.get(num,0)+1
#print(counts)
max_cnt=0
max_val=0
for k,v in counts.items():
    if v>max_val:
        max_val=v
        max_cnt=k
print(max_cnt)
