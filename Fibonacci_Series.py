# Context:
# A financial services company, FutureInvest, uses advanced mathematical
# models to forecast market trends and make investment decisions. One of the
# models they use is based on the Fibonacci sequence due to its relevance in
# technical analysis, particularly in identifying retracement levels and predicting
# future price movements.
# Scenario:
# FutureInvest analysts need a reliable tool that can generate the Fibonacci
# sequence up to a specified number of terms. This tool will help them in
# creating Fibonacci retracement levels, which are critical for predicting potential
# reversal points in the financial markets. The accuracy and efficiency of
# generating these sequences are crucial for timely and effective decisionmaking

n=int(input("enter no:"))
a,b=0,1
c=a+b
if n==1:
    print(a)
elif n==2:
    print(a)
    print(b)
else:
    print(a)
    print(b)
    for i in range(2,n):
        print(c)
        a=b
        b=c
        c=a+b


# Method 2 
def rec(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return rec(n-1)+rec(n-2)
if __name__=="__main__":
    n=int(input())
    print(rec(n))
