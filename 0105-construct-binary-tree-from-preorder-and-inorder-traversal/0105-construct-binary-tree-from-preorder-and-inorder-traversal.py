# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # preorder = Root L R
        # inorder = L Root R
        if not preorder:
            return None
        val = preorder.pop(0)
        idx = inorder.index(val)
        root = TreeNode(val)
        stack = [
            (root, 'left', preorder[:idx], inorder[:idx]),
            (root, 'right', preorder[idx:], inorder[idx+1:])]
        while stack:
            node, direction, preorder, inorder = stack.pop(0)
            if not preorder:
                continue
            val = preorder.pop(0)
            idx = inorder.index(val)
            setattr(node, direction, TreeNode(val))
            stack.extend([
                (getattr(node, direction), 'left', preorder[:idx], inorder[:idx]),
                (getattr(node, direction), 'right', preorder[idx:], inorder[idx+1:])])
        return root
        