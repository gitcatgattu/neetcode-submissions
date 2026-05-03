# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res=0
        def dfs(root,maxUp):
            if not root:
                return 
            maxUp=max(maxUp,root.val)
            dfs(root.left,maxUp)
            dfs(root.right,maxUp)
            if maxUp<=root.val:
                self.res+=1
            return 
        dfs(root,-100)
        return self.res