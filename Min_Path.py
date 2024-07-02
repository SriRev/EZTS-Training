# Start   |1|2|2|3|
#         |3|1|4|2|
#         |1|5|3|3|
#         |1|2|1|1|     End
# Find the minimum path using greedy algorithm(Method 1), Dynamic programming(Method 2) 
# Note:must move right or down

# On using greedy algorithm we get the path as 1->2->1->4->2->3->1 = 14
# But the min path is 1->3->1->1->2->1->1 = 10

# Method 1

l=[
   [1,2,2,3],
   [3,1,4,2],
   [1,5,3,3],
   [1,2,1,1]
]

n=len(l)-1
m=len(l[0])-1
i=j=0
s=l[i][j]
while i<n or j<m:
    if i==n:
        j+=1
    elif j==m:
        i+=1
    elif l[i][j+1]<l[i+1][j]:
        j+=1
    else:
        i+=1
    s+=l[i][j]
print(s)

# Method 2

dp=[
    [1,3,5,8],
    [4,4,8,10],
    [5,9,11,13],
    [6,8,9,10]
]
print(dp[n][m])