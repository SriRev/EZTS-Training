# Method 1

n=int(input("enter no:"))
f=1
if n==0:
    print("1")
else:
    for i in range(1,n+1):
        f=f*i
    print(f)



# Method 2

def fact(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else :
        return n*fact(n-1)
if __name__=="__main__":
    n=int(input("enter no:"))
    print(fact(n))
