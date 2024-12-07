from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: Optional[TreeNode]) -> int:

    if root == None:
        return 0

    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    
    return 1 + max(left_depth, right_depth)

if __name__ == '__main__':
    
    root = TreeNode(val = 3, left = TreeNode(val = 9, left = None, right= None), right= TreeNode(val= 20, left= TreeNode(val= 15, left= None, right= None), right= TreeNode(val= 7, left= None, right= None)))
    
    result = maxDepth(TreeNode(root))
    
    print(result)
