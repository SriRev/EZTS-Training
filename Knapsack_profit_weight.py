# Method 1---->Sorting

p=[5,10,15,7,8,9,4]
w=[1,3,5,4,1,3,2]
pw={}
for i in range(len(p)):
    pw[i]=p[i]/w[i]
print(pw)
l=list(pw.items())
sorted_list=sorted(l,key=lambda x:x[1],reverse=True)
print("Using lambds finction:",sorted_list)
n=len(l)
for i in range(n-1):
    max=i
    for j in range(i+1,n):
        if l[j][1]>l[max][1]:
            max=j
    l[i],l[max]=l[max],l[i]
print("Using selection sort:",l)
l.sort(key=lambda x:x[1],reverse=True)
print("Using sort fuction:",l)
spw={}
for i in l:
    spw[i[0]]=i[1]
print(spw)


# method 2---->Recursion

# def cal_max(p,w,c,n):
#     if n==0 or c==0:
#         return 0
#     if w[n-1]>c:
#         return cal_max(p,w,c,n-1)
#     else:
#         return max(p[n-1]+cal_max(p,w,c-w[n-1],n-1),cal_max(p,w,c,n-1))


# p=[5,10,15,7,8,9,4]
# w=[1,3,5,4,1,3,2]
# c=15
# n=len(p)
# print(cal_max(p,w,c,n))

# Method 3---->Memorization

# def cal_max(p,w,c,n):
#     if n==0 or c==0:
#         return 0
#     if dp[n][c]!=0:
#         return dp[n][c]
#     if w[n-1]<=c:
#         dp[n][c]=max(p[n-1]+cal_max(p,w,c-w[n-1],n-1),cal_max(p,w,c,n-1))
#         return dp[n][c]
#     else:
#         dp[n][c]=cal_max(p,w,c,n-1)
#         return dp[n][c]

# p=[5,10,15,7,8,9,4]
# w=[1,3,5,4,1,3,2]
# c=max(p)
# n=len(p)
# dp=[[0 for i in range(c+1)] for j in range(n+1)]
# print(cal_max(p,w,c,n))
# print(dp)