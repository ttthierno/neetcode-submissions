# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # do a dfs
        self.Balanced = True;
      
        def dfs(node):
            if node is None:
                return 0;
            leftH = dfs(node.left)
            rightH = dfs(node.right)

            if abs(leftH - rightH) > 1:
                self.Balanced = False

            return 1 + max(leftH, rightH)

        dfs(root)
        return self.Balanced
        
            