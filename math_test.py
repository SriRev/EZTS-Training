# Alice has a mathematics test for which she is underprepared. She has to do at least one
# question correctly to pass the test. He decides to do a question which needs her to find the
# smallest prime number which is larger than a given integer N. Your task is 
# Level 1:To find and return
# Level 2:Sum of those two numbers
# Level 3:Product of next prime numbers 
# an integer value representing the smallest prime number larger than N

# Input Format:
# input1: An integer value N
# Output Format:
# Return an integer value representing the smallest prime number larger than N.
# Sample Input
# 6
# Sample Output
# 7 

def check_prime(n):
    f=0
    if n<1:
        f=1
    elif n==1:
        f=0
    else:
        for i in range(2,(n//2)+1):
            if n%i==0:
                f=1
                break
    if f==0:
        return 1
    else:
        return 0
r=[]
n=int(input("enter a no:"))
flag=0
k=n+1
while flag<1:
    flag=check_prime(k)
    if flag==1:
        r.append(k)
    else:
        k=k+1
sum=0
for i in range(n+1,k):
    sum+=i
r.append(sum)
p1=k
flag=0
k=p1+1
while flag<1:
    flag=check_prime(k)
    if flag==1:
        p2=k
    else:
        k=k+1
p3=p1*p2
flag=check_prime(p3)
if flag==0:
    r.append(False)
else:
    r.append(True)
p=tuple(r)
print(p)