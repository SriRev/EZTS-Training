def t(x):
    mid=len(x)//2
    if sum(x[:mid:])==sum(x[mid::]):
        return 1
    elif sum(x[:mid-1:])==sum(x[mid-1::]):
        return 1
    elif sum(x[:mid+1:])==sum(x[mid+1::]):
        return 1
    


l=[[2,2,1,2,1],[1,1,1,1,1]]
for i in l:
    if t(i)==1:
        print('Found')
    else:
        print("Found at",len(i)//2)