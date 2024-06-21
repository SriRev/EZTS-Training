# Method 1
s=str(input("Enter string:"))
ca=0
ce=0
ci=0
co=0
cu=0
for i in s:
    if i=='a' or i=='A':
        ca+=1
    elif i=='e' or i=='E':
        ce+=1
    elif i=='i' or i=='I':
        ci+=1
    elif i=='o' or i=='O':
        co+=1
    elif i=='u' or i=='U':
        cu+=1
    else:
        pass
print(f"a={ca} e={ce} i={ci} o={co} u={cu}")
l=[ca,ce,ci,co,cu]
print(l)
print(max(l))

# Method 2
def count_vowel(s): 
    dic={'A':0,'E':0,'I':0,'O':0,'U':0}
    
    for i in s:
        if i=='a' or i=='A':
            dic['A']+=1
        elif i=='e' or i=='E':
            dic['E']+=1
        elif i=='i' or i=='I':
            dic['I']+=1
        elif i=='o' or i=='O':
            dic['O']+=1
        elif i=='u' or i=='U':
            dic['U']+=1
    x=max(dic.values())
    r=[]
    for i,j in dic.items():
        if j==x:
            r.append(i)
    return r
i_p=[
    ["Srinivas","In class"],
    ["Sanath","He is a guy"],
    ["Kartik","He is doing coding"]]

o_p={}
for i in i_p:
    o_p[i[0]]=count_vowel(i[1]) #r
print(o_p)    
