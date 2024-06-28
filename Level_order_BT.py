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

def level_order(root):
    q=[root]
    q.append(None)
    while len(q)!=0:
        c=q.pop(0)
        if c==None:
            if len(q)==0:
                return
            else:
                print()
                q.append(None)
        else:
            print(c.value,end=' ')
            if c.left!=None:
                q.append(c.left)
            if c.right!=None:
                q.append(c.right)

        
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
    root.right.right=node(8)

    root.right.right.right=node(11)

level_order(root)