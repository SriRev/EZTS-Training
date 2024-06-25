#               1
#            /    \
#           2      3
#          / \    / \
#         4   5  6   7
#            / \      \
#           9   10     11
#          / \
#         12  13

class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
class node_data:
    def __init__(self,Node,Hkey):
        self.node=Node
        self.hkey=Hkey

def top_view(root):
    temp=node_data(root,0)
    q=[temp]
    q.append(None)
    key_dict={}

    while len(q)!=0:
        c=q.pop(0)
        if c==None:
            if len(q)==0:
                break
            else:
                q.append(None)
        else:
            if c.hkey not in key_dict.keys():
                key_dict[c.hkey]=c.node.value
            if c.node.left!=None:
                temp=node_data(c.node.left,c.hkey-1)
                q.append(temp)
            if c.node.right!=None:
                temp=node_data(c.node.right,c.hkey+1)
                q.append(temp)

    for i in sorted(key_dict):
        print(key_dict[i])
    print(key_dict)   
if __name__=="__main__":
    root=node(1)
    root.left=node(2)
    root.right=node(3)


    root.left.left=node(4)
    root.left.right=node(5)

    root.left.right.left=node(9)
    root.left.right.right=node(10)
    root.left.right.right.left=node(12)
    root.left.right.right.right=node(13)
    
    root.right.left=node(6)
    root.right.right=node(7)

    root.right.right.right=node(11)
 
top_view(root)