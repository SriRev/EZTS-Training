#              1
#            /   \
#           2     3
#          / \   / \
#         4   5 6   7 


class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None

def height(root):
    if root==None:
        return 0
    lh=height(root.left)
    rh=height(root.right)
    return max(lh,rh)+1

if __name__=="__main__":
    root=node(1)
    root.left=node(2)
    root.right=node(3)

    root.left.left=node(4)
    root.left.right=node(5)
    
    root.right.left=node(6)
    root.right.right=node(7)
print(height(root))