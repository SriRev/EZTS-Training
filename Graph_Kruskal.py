g=[
    [0,7,-1,-1,-1,-1,-1,2,-1,-1],
    [7,0,4,1,-1,5,-1,-1,-1,-1],
    [-1,4,0,-1,-1,-1,-1,8,-1,-1],
    [-1,1,-1,0,6,8,3,3,-1,-1],
    [-1,-1,-1,6,0,-1,-1,6,8,-1],
    [-1,5,-1,8,-1,0,-1,-1,-1,-1],
    [-1,-1,-1,3,-1,-1,0,-1,9,2],
    [2,-1,8,3,6,-1,-1,0,-1,-1],
    [-1,-1,-1,-1,8,-1,9,-1,0,-1],
    [-1,-1,-1,-1,-1,-1,2 -1,-1,0]
]
v=[False]*len(g)
min=float("inf")
x=y=-1
for i in range(len(g)):
    for j in range(len(g[i])):
        if g[i][j]==0 or g[i][j]<0:
            continue  
        elif min>g[i][j]:
            min=g[i][j]
            x=i
            y=j
print(x+1,y+1,min)
v[x]=True
v[y]=True
mst=[]
mst.append(tuple((x+1,y+1,min)))
while False in v:
    min=float("inf")
    for i in range(len(v)):
            for j in range(len(g[i])):
                if g[i][j]==0 or g[i][j]==-1 or v[j]==True:
                    continue  
                elif min>g[i][j]:
                    min=g[i][j]
                    x=i
                    y=j
    v[y]=True
    mst.append(tuple((x+1,y+1,min)))
print(mst)
print(v)
