# Quick Sort
# pivot:last element of the array
# if i found smaller than pivot then increase j by one and swap it by j 
# if i found bigger than pivot then do nothing


def partation(L,Low,High):
    P=L[High]
    Pi=High
    j=Low-1
    for i in range (Low,High):
        if L[i]<=P:
            j+=1
            L[i],L[j]=L[j],L[i]
    j+=1
    L[j],L[Pi]=L[Pi],L[j]
    Pi=j
    return Pi

def Quick_Sort(L,Low,High):
    if Low<High:
        pi=partation(L,Low,High)
        Quick_Sort(L,Low,pi-1)
        Quick_Sort(L,pi+1,High)
    return    


if __name__=="__main__":
    L=list(map(int,input("Enter list:").split()))
    low=0
    high= len(L)-1
    Quick_Sort(L,low,high)

    print("Sorted Array = ",L)