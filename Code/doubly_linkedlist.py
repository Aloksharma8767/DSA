class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class doubly_linkedlist:
    def __init__(self):
        self.head=None
#method to insert node at end of the linkedlist
    def insert_node_at_end(self,data):
        new_node=Node(data) #object of the Node class
        if self.head is None:
            self.head=new_node
            return
        else:
            a=self.head
            while a.next is not None:
                a=a.next
            a.next=new_node
            new_node.prev=a
#method to insert node at the beginning of the linkedlist
    def  insert_node_at_beginning(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        else:
            a=self.head
            a.prev=new_node
            new_node.next=self.head
            self.head=new_node
#method to insert node at specific index
    def insert_node_at_specific_index(self,data,index):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        else:
            a=self.head
            for i in range(1,index-1):
                a=a.next
            new_node.next=a.next
            a.next.prev=new_node
            a.next=new_node
            new_node.prev=a
#method to delete the node at beginning of linkedlist
    def deletion_of_node_at_beginning(self):
        a=self.head
        self.head=a.next
        a.next.prev=None
        a.next=None
#deletion of node at the end of linkedlist 
    def deletion_of_node_at_end(self):
        prev=self.head
        a=prev.next
        while a.next is not None:
            a=a.next
            prev=prev.next
        prev.next=None
#deletion of the node at specific index of the linkedlist
    def deletion_of_node_at_specific_index(self,index):
        prev=self.head
        a=prev.next
        for i in range(1,index-1):
            a=a.next
            prev=prev.next
        prev.next=a.next
        a.next.prev=prev
#method to travers forward in linkedlist
    def travers_forward(self):
        a=self.head
        while a is not None:
            print(a.data,"->",end=" ")
            a=a.next 
#method to traverse backward in linkedlist
    def travers_backword(self):
        print()
        a=self.head
        while a.next is not None:
            a=a.next
        while a is not None:
            print(a.data,"<-",end=" ")
            a=a.prev
#method to print the size of linkedlist
    def size_of_linkedlist(self):
        a=self.head
        size=0
        while (a):
            size=size+1
            a=a.next
        return size
#method to update the value of any specific linkedlist node
    def update_node(self,val,index):
        a=self.head
        for i in range(1,index):
            a=a.next
        a.data=val
#creating the object of doublylinkedlist class
n=doubly_linkedlist()
n.insert_node_at_end(6)
n.insert_node_at_end(7)
n.insert_node_at_end(8)
n.insert_node_at_end(9)
n.insert_node_at_beginning(1)
n.insert_node_at_beginning(2)
n.insert_node_at_beginning(4)
n.insert_node_at_beginning(5)
n.insert_node_at_specific_index(3,3)
print("Size of linkedlist is :",n.size_of_linkedlist())
n.update_node(10,5)
# n.deletion_of_node_at_specific_index(4)
# n.deletion_of_node_at_beginning()
# n.deletion_of_node_at_end()
n.travers_forward()
n.travers_backword()
