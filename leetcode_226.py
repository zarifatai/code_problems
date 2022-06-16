from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            # to reduce line length and increase readability
            invert = self.invert_tree
            root.left, root.right = invert(root.right), invert(root.left)
            return root
