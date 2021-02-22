# V1
# 执行用时：36 ms, 在所有 Python3 提交中击败了92.84%的用户
# 内存消耗：15.1 MB, 在所有 Python3 提交中击败了9.97%的用户


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def help(self, p, q):
        if p == None and q == None: return True
        if p and q and p.val == q.val:
            return self.help(p.right, q.left) and self.help(p.left, q.right)
        return False

    def isSymmetric(self, root: TreeNode) -> bool:
        if root:
            return self.help(root.left, root.right)
        return True