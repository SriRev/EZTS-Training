# method 1
l=[2,4,3,5,6,3,4,6,7,1,2,5]
sum=max=0
for i in range(0,len(l)-2):
    sum=l[i]+l[i+1]+l[i+2]
    if max<sum:
        max=sum
        pos=i
print(max,l[pos],l[pos+1],l[pos+2])

# method 2

l=[2,4,3,5,6,3,4,6,7,1,2,5]
sum=max=0
k=int(input("Enter the no:"))
for i in range(0,len(l)-k+1):
    sum=0
    for j in range(0,k):
        sum+=l[i+j]
    if max<sum:
            max=sum
            pos=i
print(max)
for j in range(0,k):
    print(l[pos+j],end=' ')
    print()

# Method 3:Window sliding technique
l=[2,3,4,5]
window=max=0
k=int(input("Enter the no:"))
for j in range(0,k):
     window+=l[j]
for i in range(0,len(l)-k):
    if max<window:
         max=window
         pos=i
    window=window+l[i+k]-l[i]
print(max)
