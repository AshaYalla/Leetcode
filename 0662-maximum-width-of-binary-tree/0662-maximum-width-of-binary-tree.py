class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        maxWidth = 0
        
        q = deque()
        q.append((root, 0))
        
        while q:
            qlen = len(q)
            x, leftIndex = q[0]
            
            for i in range(qlen):
                node, nodeIndex = q.popleft()
                if node.left:
                    q.append((node.left, 2*nodeIndex))
                if node.right:
                    q.append((node.right, 2*nodeIndex + 1))
            
            maxWidth = max(maxWidth, nodeIndex - leftIndex + 1)
        
        return maxWidth