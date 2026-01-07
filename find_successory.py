class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    if node.right != None:
        next = node.right
        while next.left != None:
            next = next.left
        return next
    elif node.parent != None:
        if node.parent.left == node:
            return node.parent
        return node.parent.parent
    return None
