# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root,lv,rv):
            if not root:
                return True
            if lv>=root.val or root.val>=rv:
                return False
            return dfs(root.left,lv,root.val) and dfs(root.right,root.val,rv)
        return dfs(root,float('-inf'),float('inf'))
        

