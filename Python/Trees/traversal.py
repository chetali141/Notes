"""
Traverse the tree using pre order, post order and in order traversal
1. Pre order: root, left, right
    Space complexity = O(H) ... H is height of the binary tree
    Time complexity = O(N)
2. Post order: left, right, root
3. In order: left, root, right
"""

import treeNode

def preOrder(root):
    if root is None:
        return 
    print(root.val)
    preOrder(root.left)
    preOrder(root.right)

def postOrder(root):
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.val)


def inOrder(root):
    if root is None:
        return
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)

# root = treeNode.TreeNode(1)
# root.left = treeNode.TreeNode(2)
# root.right = treeNode.TreeNode(3)
# root.left.left = treeNode.TreeNode(4)
# root.left.right = treeNode.TreeNode(5)

# preOrder(root)
# print("-------")
# postOrder(root)
# print("-------")
# inOrder(root)
