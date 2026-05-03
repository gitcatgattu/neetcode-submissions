# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBal=True
        def height(root):
            if not root:
                return 0
            left=height(root.left)
            right=height(root.right)
            diff=abs(left-right)
            self.isBal=diff<=1 and self.isBal
            return max(height(root.left),height(root.right))+1
        
        height(root)
        return self.isBal

        