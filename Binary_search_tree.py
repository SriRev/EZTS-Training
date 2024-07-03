# Method 1
    #         4
    #        / \
    #       3   6
    #      /   / \
    #     2   5   7
    #    /         \
    #   1           8
    #                \
    #                 9


# l=[4,6,7,3,8,2,5,9,1]

class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None

def bst(value,root):
    if root==None:
        root=node(value)
    if root.value<value:
        if root.right==None:
            root.right=node(value)
        else:
            bst(value,root.right)
    else:
        if root.left==None:
            root.left=node(value)
        else:
            bst(value,root.left)

def add():
    l=[4,6,7,3,8,2,5,9,1]
    root=node(l[0])
    l.pop(0)
    for i in l:
        bst(i,root)
    return root
def preorder(root):
    if root==None:
        return
    print(root.value,end=' ')
    preorder(root.left)
    preorder(root.right)

root=add()
preorder(root)

# Method 2
print()
class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
def inst_bst(root,value):
    if root==None:
        node(value)
    if value>root.value:
        inst_bst(root.left,value)
    if value>root.value:
        inst_bst(root.right,value)
    return root

def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.value,end=' ')
    inorder(root.right)

l=[4,6,7,3,8,2,5,9,1]
root=node(l[0])
l.pop(0)
for i in l:
    bst(i,root)
inorder(root)

