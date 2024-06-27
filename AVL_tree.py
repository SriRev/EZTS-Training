# 19,99,75,7,21,34,38,27,134,100,29,0,12,17,143

#             34
#            /  \
#           /    \
#          /      \
#         /        \
#        /          \
#       21          100
#      /  \        /   \
#     7    27     75    134
#    / \     \   /  \      \
#   0   17   29 38   99     143
#      /  \
#     12   19


class node:
    def __init__(self,data) -> None:
        self.val=data
        self.left=None
        self.right=None
        self.height=1

def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)
    
def insert(root,super):
    if not root:
        return node(super)
    if super <root.val:
        root.left=insert(root.left,super)
    else:
        root.right=insert(root.right,super)       
    root.hieght=1+max(ght(root.left),ght(root.right))
    
    bf=getbf(root)
    if bf>1 and super<root.left.val:              #rr rotation
        return rightRotate(root)

    if bf>1 and super>root.left.val:              #rl rotation
        root.left=leftRotate(root)
        return rightRotate(root)        

    if bf<-1 and super>root.right.val:              #ll rotation
        return leftRotate(root)

    if bf<-1 and super<root.left.val:                  #lr rotation
        root.right=rightRotate(root)
        return leftRotate(root)  

    return root
def ght(root):
    if not root:
        return 0
    return root.height
def getbf(root):
    if not root:
        return 0
    return ght(root.left)-ght(root.right)
def leftRotate(a):
    b=a.right
    temp=b.left
    
    b.left=a
    a.right=temp
    
    a.height=1+max(ght(a.left),ght(a.right))
    b.height=1+max(ght(b.left),ght(b.right))
    return b
def rightRotate(a):
    b=a.left
    temp=b.right
    
    b.right=a
    a.left=temp
    
    a.height=1+max(ght(a.left),ght(a.right))
    b.height=1+max(ght(b.left),ght(b.right)) 
    return b  

if __name__=="__main__":
    
    vl=[19,99,75,7,21,34,38,27,134,100,29,0,12,17,143]
    root=None
    for i in vl:
        root=insert(root,i)
    inorder(root)