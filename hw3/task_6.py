from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """Сложность функции O(n)"""
        self.diameter = 0
        def height(node):
            left = height(node.left) if node.left else 0
            right = height(node.right) if node.right else 0
            if left + right > self.diameter:
                self.diameter = left + right
            return 1 + max(left, right)
        height(root)
        return self.diameter
