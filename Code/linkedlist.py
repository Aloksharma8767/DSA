class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
#method to add node at end of linkedlist
    def insertatend(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            last_node=self.head
            while last_node.next is not None:
                last_node=last_node.next
            last_node.next=new_node
# Method to add a node at begin of LL
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    def traversal(self):
        last_node=self.head
        while last_node:
            print(last_node.data,"->",end=" ")
            last_node=last_node.next
#method to add node at specific position
    def insert_at_specific_position(self,data,position):
        if position<0:
            print("invalid position given ")
            return
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        a=self.head
        for i in range(1,position-1):
            a=a.next
        new_node.next=a.next
        a.next=new_node
    # def insertAtIndex(self, data, index):
    #     new_node = Node(data)
    #     current_node = self.head
    #     position = 1
    #     if position == index:
    #         self.insertAtBegin(data)
    #     else:
    #         while(current_node != None and position != index):
    #             position = position+1
    #             current_node = current_node.next
 
    #         if current_node != None:
    #             new_node.next = current_node.next
    #             current_node.next = new_node
    #         else:
    #             print("Index not present")
    def deletion_at_beginning(self):
        print()
        a=self.head
        self.head=a.next
        a.next=None
    def deletion_at_end(self):
        print()
        prev=self.head
        n=prev.next
        while n.next is not None:
            n=n.next
            prev=prev.next
        prev.next=None
    def delete_at_specific_position(self,position):
        print()
        prev=self.head
        a=prev.next
        for i in range(1,position):
            a=a.next
            prev=prev.next
        prev.next=a.next
        a.next=None
        
        
n=linkedlist()
n.insertatend(1)
n.insertatend(2)
n.insertatend(3)
n.insertatend(4)
n.insertAtBegin(9)
n.insertAtBegin(8)
n.insertAtBegin(7)
n.insert_at_specific_position(12,3)
# n.insertAtIndex(12,2)
n.traversal()
# n.deletion_at_beginning()
# n.deletion_at_end()
n.delete_at_specific_position(3)
n.traversal()

        
