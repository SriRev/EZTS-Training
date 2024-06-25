#               1
#            /    \
#           2      3
#            \      \
#             4      8
#            /        \
#           5          9
#          / \        /
#         6   7      10
#                   /
#                  11

class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
class node_data:
    def __init__(self,node,Hkey):
        self.node=node
        self.hkey=Hkey

def bottom_view(root):
    temp=node_data(root,0)
    q=[temp]
    key_dict={}

    while len(q)!=0:
        c=q.pop(0)
        key_dict[c.hkey]=c.node.value
        if c.node.left is not None:
                temp=node_data(c.node.left,c.hkey-1)
                q.append(temp)
        if c.node.right is not None:
                temp=node_data(c.node.right,c.hkey+1)
                q.append(temp)

    for i in sorted(key_dict):
        print(key_dict[i])
    print(key_dict)   
if __name__=="__main__":
    root=node(1)
    root.left=node(2)
    root.right=node(3)


    root.left.right=node(4)

    root.left.right.left=node(5)
    root.left.right.left.left=node(6)
    root.left.right.left.right=node(7)

    root.right.right=node(8)
    root.right.right.right=node(9)
    root.right.right.right.left=node(10)
    root.right.right.right.left.left=node(11)
    
bottom_view(root)