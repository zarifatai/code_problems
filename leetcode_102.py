class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# bfs
def level_order(root):
    res = []
    q = collections.deque([root])

    while q:
        len_q = len(q)
        level = []

        for _ in range(len_q):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)

        if level:
            res.append(level)

    return res
