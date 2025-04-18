"""
Given two binary trees. 
Return true if they are symmetric (i.e. mirror image)

Approach: Use traversal
TC = O(N)
SC = O(H)
"""

import treeNode

def symmetric(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None: 
        return False
    return (root1.val == root2.val and symmetric(root1.left, root2.right) and symmetric(root1.right, root2.left))


root1 = treeNode.TreeNode(10)
root1.left = treeNode.TreeNode(15)
root1.right = treeNode.TreeNode(7)
root1.left.left = treeNode.TreeNode(8)
root1.left.right = treeNode.TreeNode(2)
root1.right.left = treeNode.TreeNode(20)

root2 = treeNode.TreeNode(10)
root2.left = treeNode.TreeNode(15)
root2.right = treeNode.TreeNode(7)
root2.left.left = treeNode.TreeNode(8)
root2.left.right = treeNode.TreeNode(2)
root2.right.left = treeNode.TreeNode(20)

root3 = treeNode.TreeNode(10)
root3.left = treeNode.TreeNode(15)
root3.right = treeNode.TreeNode(7)
root3.left.left = treeNode.TreeNode(8)
root3.left.right = treeNode.TreeNode(12)

root4 = treeNode.TreeNode(10)
root4.left = treeNode.TreeNode(7)
root4.right = treeNode.TreeNode(15)
root4.right.left = treeNode.TreeNode(2)
root4.right.right = treeNode.TreeNode(8)
root4.left.right = treeNode.TreeNode(20)

print(symmetric(root1, root2))
print(symmetric(root1, root3))
print(symmetric(root1, root4))
