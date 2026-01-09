class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def get_values(node):
    if node is None:
        return []
    return [node.value] + get_values(node.left) + get_values(node.right)

def findKthLargestValueInBst(tree, k):
    results = get_values(tree)        
    results.sort(reverse=True)
    print(results)
    return results[k - 1]
