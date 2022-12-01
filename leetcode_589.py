class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def preorder(root):
    output = []

    output = dfs(root, output)
    return output


def dfs(root, output):
    if root is None:
        return

    output.append(root.val)

    for child in root.children:
        self.dfs(child, output)

    return output
