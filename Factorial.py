n=int(input("enter no:"))
for i in range(n):
    print(n)
    i+=1
# print(x)

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