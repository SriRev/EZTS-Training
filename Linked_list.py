class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head=None

    def traverse(self):
        if self.head==None:
            print("\nLinked List is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"->",end=" ")
                n=n.ref

    def add_begin(self,data):
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node

    def add_end(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:    
                n=n.ref
            n.ref=new_node

    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if n.data==x:
                break
            else:
                n=n.ref
        if n is None:
            print("\nNode is not present in LL")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node

    def add_before(self,data,x):
        if self.head is None:
            print("\nLL is empty")
            return
        if self.head==x:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            else:
                n=n.ref
        if n is None:
            print("\nNode is not present in LL")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node

    def del_begin(self):
        if self.head is None:
            print("\nLL is empty")
        else:
            self.head=self.head.ref

    def del_end(self):
        if self.head is None:
            print("\nLL is empty")
        elif self.head.ref==None:
            self.head=None
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None

    def del_value(self,x):
        if self.head is None:
            print("\nLL is empty")
            return
        if self.head.data==x:
            self.head=None
            return
        else:
            n=self.head
            while n.ref.ref is not None:
                if n.ref.data==x:
                    break
                n=n.ref
            if n.ref is None:
                print("\nNode not found")
            else:
                n.ref=n.ref.ref


LL=LinkedList()
while True:
    print("\n1.ADD\n2.DELETE\n3.DISPLAY\n4.EXIT\n")
    ch=int(input("Enter your choice: "))
    if ch==1:
        print("\n1.ADD BEGIN\n2.ADD END\n3.ADD AFTER\n4.ADD BEFORE")
        choice=int(input("\nchoose to add element: "))
        data=int(input("\nElement: "))
        if choice==1:
            LL.add_begin(data)
        elif choice==2:
            LL.add_end(data)
        elif choice==3:
            x=int(input("enter x: "))
            LL.add_after(data,x)
        elif choice==4:
            x=int(input("enter the value present in LL: "))
            LL.add_before(data,x)
        else:
            print("INVALID CHOICE")

    elif ch==2:
        print("\n1.DELETE BEGIN\n2.DELETE END\n3.DELETE ELEMENT")
        choice=int(input("\nchoose to add element: "))
        if choice==1:
            LL.del_begin()
        elif choice==2:
            LL.del_end()
        elif choice==3:
            data=int(input("\nElement: "))
            LL.del_value(data)
        else:
            print("INVALID CHOICE")

    elif ch==3:
        LL.traverse()

    elif ch==4:
        break

    else:
        print("INVALID CHOICE")