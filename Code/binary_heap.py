class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    def insert(self,num):
        if self.data is None:
            self.data=num
        