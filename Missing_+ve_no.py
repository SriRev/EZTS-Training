def positive(n):
    n.sort()
    res=1
    for i in n:
        if res==i:
            res+=1
    return res
n=list(map(int,input("Enter the list:").split()))
print(positive(n))