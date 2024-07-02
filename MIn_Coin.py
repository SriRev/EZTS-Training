# Avialable denomination:1,5,7
# Target:18
# What will be the mim coin requied to to reach the Target

# Method 1-->Greedy

c=[1,5,7]
t=18
count=0
i=len(c)-1
while t!=0:
    if t>=c[i]:
        t=t-c[i]
        count+=1
    elif t<c[i]:
        i-=1
print(count) #6

# Method 2-->DP

coins = [1, 5, 7]
target = 18
dp = [float('inf')] * (target + 1)
dp[0] = 0

for i in range(1, target + 1):
    for coin in coins:
        if i >= coin:
            dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[target]) #4