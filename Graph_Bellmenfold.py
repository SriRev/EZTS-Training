# Method 1--->Argency Matrix
g=[
    [0,6,4,5,False,False],
    [False,0,False,False,-1,False],
    [False,-2,0,False,3,False],
    [False,False,-2,0,False,-1],
    [False,False,False,False,0,3],
    [False,False,False,False,False,0]
]
# d={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F'}
el=[]
for i in range(len(g)):
    for j in range(len(g[i])):
        if g[i][j]!=False and g[i][j]!=0:
            el.append(tuple((i,j)))
print(el)
dist={}
for i in range(len(g)):
    dist[i]=float("inf")
dist[0]=0

for i in range(len(g)-1):
    for j in el:
        ndist=dist[j[0]]+g[j[0]][j[1]]
        if dist[j[1]]>ndist:
            dist[j[1]]=ndist
print(dist)
        
print("-"*110)

# Method 2--->Argency list
def bellmanford(v,e):
    a='ABCDEF'
    l={}
    d=l.fromkeys(a,float('inf'))
    d['A']=0
    for _ in range(v-1):
      for u,v,w in e:
         if d[u]+w<d[v]:
            d[v]=d[u]+w
    return d

if __name__ == "__main__":
    V = 6
    S = 0
    edges = [
        ('A','B',6),
        ('A','C',4),
        ('A','D',5),
        ('B','E',-1),
        ('C','B',-2),
        ('C','E',3),
        ('D','C',-2),
        ('D','F',-1),
        ('E','F',3)
    ]
    d=bellmanford(V,edges)
    print(d)
