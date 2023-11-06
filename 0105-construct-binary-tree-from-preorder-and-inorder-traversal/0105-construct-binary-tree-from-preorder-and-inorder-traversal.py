class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        if len(preorder) == 0 or len(inorder) == 0:
            return None
        root = preorder[0]
        ind = inorder.index(root)
        
        node = TreeNode(root)
        node.left = self.buildTree(preorder[1:ind+1], inorder[0:ind])
        node.right = self.buildTree(preorder[ind+1:], inorder[ind+1:])
        return node

