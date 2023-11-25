class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete_node(root, key):
    if root is None:
        return root
    
    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        temp = minValueNode(root.right)
        root.val = temp.val
        root.right = delete_node(root.right, temp.val)
    
    return root

# Example usage
if __name__ == "__main__":
    root = None
    keys = [15, 10, 20, 8, 12, 17, 25]
    
    for key in keys:
        root =insert(root,key)
    
    print("Inorder traversal before deletion:")
    inorder_traversal(root)
    
    key_to_delete = 100
    root=delete_node(root,key_to_delete)
    
    print("\nInorder traversal after deleting", key_to_delete)
    inorder_traversal(root)
