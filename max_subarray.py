
def max_subarray():
    l=[4,-1,-3,-2,6,-1,-2,3,2,-8,-2]
    j=0
    ms_1=l[0]
    ms_2=l[0]
    for i in range(1,len(l)):
        ms_1=max(l[i],ms_1+l[i])
        ms_2=max(ms_1,ms_2)
    return ms_2

print(max_subarray())
