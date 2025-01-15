"""
Find if an element 'k' is present in a tree or not.

Time complexity: O(N)
Space complexity: O(H)
"""

import treeNode

def findElement(root, k):
    if root is None:
        return False
    if root.val == k:
        return True
    return findElement(root.left,k)or findElement(root.right, k) 


root = treeNode.TreeNode(10)
root.left = treeNode.TreeNode(15)
root.right = treeNode.TreeNode(7)
root.left.left = treeNode.TreeNode(8)
root.left.left.left = treeNode.TreeNode(9)
root.left.right = treeNode.TreeNode(2)
root.right.left = treeNode.TreeNode(1)
root.right.left.right = treeNode.TreeNode(14)
root.right.right = treeNode.TreeNode(12)

print(findElement(root, 20))
print(findElement(root, 7))
