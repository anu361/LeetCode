# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder, postorder):
        index = {value: i for i, value in enumerate(inorder)}

        def build(left, right):
            if left > right:
                return None

            root_val = postorder.pop()
            root = TreeNode(root_val)

            mid = index[root_val]

            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)