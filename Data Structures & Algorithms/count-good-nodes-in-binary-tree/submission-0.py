# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cur = root
        maxV = root.val
        self.ans = 0
        def dfs(node, maxV):
            if not node:
                return None
            if node.val >= maxV:
                self.ans += 1
                maxV = node.val
            dfs(node.left, maxV)
            dfs(node.right, maxV)
        
        dfs(cur, maxV)
        return self.ans

        