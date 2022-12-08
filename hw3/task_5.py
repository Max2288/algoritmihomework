from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """Сложность данной функции O(n)."""
        stack = {(root, str(root.val))}
        lst = []
        while stack:
            rt, s = stack.pop()
            if rt.left and rt.right:
                stack.add((rt.left, s+"->"+str(rt.left.val)))
                stack.add((rt.right, s+"->"+str(rt.right.val)))
            elif rt.left and not rt.right:
                stack.add((rt.left, s+"->"+str(rt.left.val)))
            elif rt.right and not rt.left:
                stack.add((rt.right, s+"->"+str(rt.right.val)))
            else:
                lst.append(s)
        return lst
