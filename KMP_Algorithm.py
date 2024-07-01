def kmp(p,s):
    m=len(p)
    n=len(s)
    lps=[]
    LPS(p,m,lps)
    print(lps)
    i=0
    j=0
    while(n-i)>=(m-j):
        if p[j]==s[i]:
            i+=1
            j+=1
        if j==m:
            print("Pattren found:",i-j)
            j=lps[j-1]
        elif i<n and p[j]!=s[i]:
            if j!=0:
                j=lps[j-1]
            else:
                i+=1


def LPS(p,m,lps):
    lps.append(0)
    j=0
    for i in range(1,m):
        if s[i]==p[j]:
            lps.append(j+1)
            j=j+1
        else:
            j=0
            lps.append(j)


if __name__=="__main__":
    s="CDEABABCABCABCABDAA"
    p="ABCAB"
    kmp(p,s)