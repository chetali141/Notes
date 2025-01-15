"""
Basic structure depicting
1. how to implement tree
2. count the number of nodes in a tree
3. find the height of the tree
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def countNodes(root):
    if root is None:
        return 0
    return countNodes(root.left) + 1 + countNodes(root.right)

def height(root):
    if root is None:
        return 0
    lheight = height(root.left)
    rheight = height(root.right)
    return max(lheight, rheight) + 1
    
# root = TreeNode(1)
# child1 = TreeNode(2)
# child2 = TreeNode(3)
# root.left = child1
# root.right = schild2
# child1.left = TreeNode(4)
# child1.right = TreeNode(5)

# print(countNodes(root))
# print(height(root))
