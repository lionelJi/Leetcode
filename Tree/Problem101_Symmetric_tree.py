# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root) -> bool:
        def judge(left, right):
            if not left and not right:
                return True
            if left and not right or right and not left:
                return False
            if left.val != right.val:
                return False

            return judge(left.left, right.right) and judge(left.right, right.left)

        if not root:
            return True

        return judge(root.left, root.right)

