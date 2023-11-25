class Node:
   def __init__(self, item):
      self.item = item
      self.left = None
      self.right = None
   def insert(self,data):
      if self.item is None:
         self.item=data
         return
      if data<self.item:
         if self.left:
            self.left.insert(data)
      else:
         self.left=Node(data)
      if data>self.item:
         if self.right:
            self.right.insert(data)
      else:
         self.right=Node(data)
   def preorder(self):
         print(self.item,end=" ")
         if self.left:
            self.left.preorder()
         if self.right:
            self.right.preorder()
   def inorder(self):
      if self.left:
         self.left.inorder()
      print(self.item,end=" ")
      if self.right:
         self.right.inorder()
   def postorder(self):
      if self.left:
         self.left.postorder()
      if self.right:
         self.right.postorder()
      print(self.item,end=" ")
   def search(self,data):
      if self.item==data:
         print("node is found")
         return
      if data<self.item:
         if self.left:
            self.left.search(data)
         else:
            print("node is not present on left side")
      else:
         if self.right:
            self.right.search(data)
         else:
            print("node is not  present on right side")
   def delete(self,data):
      if self.item is None:
         print("Tree is empty")
         return
      if data<self.item:
         if self.left:
            self.left=self.left.delete(data)
         else:
            print("Data is not present in tree")
      elif data>self.item:
         if self.right:
            self.right=self.right.delete(data)
         else:
            print("Data is not present in the tree")
      else:
         if self.left is None:
            temp=self.right
            self=None
            return temp
         if self.right is None:
            temp=self.left
            self=None
            return temp
         node=self.right
         while node.left:
            node=node.left
         self.item=node.item
         self.right=self.right.delete(node.item)
      return self

ra=Node(8)
v=[5,3,6,2,4,11,10,12,9]
for i in v:
   ra.insert(i)
ra.preorder()
# print()
# ra.inorder()
# print()
# ra.postorder()
# ra.search(50)
print()
ra.delete(5)
print()
ra.preorder()