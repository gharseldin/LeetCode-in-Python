
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if target is None:
            return None
        cache = []
        cache.append(cloned)
        while len(cache) is not 0:
            node = cache.pop()
            if node is not None:
                if node.val == target.val:
                    return node
                else:
                    cache.append(node.left)
                    cache.append(node.right)
        return None
