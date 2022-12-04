class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root, floor=float("-inf"), celing=float("inf")):
    if not root:
        return True
    if root.val <= floor or root.val >= ceiling:
        return False
    return is_valid_bst(root.left, floor, root.val) and is_valid_bst(
        root.right, root.val, ceiling
    )
