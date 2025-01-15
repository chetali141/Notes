"""
Given a tree.
invert the tree or create the mirror image of the tree.
"""

import treeNode

def mirrorTree(root):
    if root is None:
        return None
    left = mirrorTree(root.left)
    right = mirrorTree(root.right)

    root.right = left
    root.left = right

    return root

def inOrder(root):
    if root is None:
        return
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)

# In order traversal of tree before inverting it: 2 1 4 3 5, after inverting it: 5 3 4 1 2
root = treeNode.TreeNode(1)
root.left = treeNode.TreeNode(2)
root.right = treeNode.TreeNode(3)
root.right.left = treeNode.TreeNode(4)
root.right.right = treeNode.TreeNode(5)

invertedRoot = mirrorTree(root)
inOrder(root)
