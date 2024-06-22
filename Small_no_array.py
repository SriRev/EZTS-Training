# Find the min +ve integer in an array

def small(l):
    res=999
    for i in l:
        if i>0 and i<res:
            res=i
    print(res)
              
l=list(map(int,input("Enter the list:").split()))
small(l)


