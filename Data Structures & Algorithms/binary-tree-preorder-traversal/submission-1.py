# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        res = []

        stack = []
        stack.append(root)
        
        while len(stack) > 0:
            curr = stack.pop()

            if curr.right is not None:
                stack.append(curr.right)
        
            if curr.left is not None:
                stack.append(curr.left)

            res.append(curr.val)


        return res