class Solution:
    def isSubtree(self, root, subRoot) :
        ans = False
        cur = root
        cur2 = subRoot
        def compare(tree1,tree2):
            if not tree1 and not tree2:
                return True
            
            if tree1 and tree2 and tree1.val == tree2.val:
                return compare(tree1.left, tree2.left) and compare(tree1.right, tree2.right)
            return False
                
            
        
        def dfs(cur):
            dfs(cur.left)
            if cur.val == subRoot.val and compare(cur,cur2 ):
                return True
                
            dfs(cur.right)
            return False
            
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        if not subRoot: return True
        if not root : return False
        
        if self.sameTree(root , subRoot):
            return True
        return (self.isSubtree(root.left , subRoot) or self.isSubtree(root.right , subRoot) )
        
        
    def sameTree(self,s,t):
        if not s and not t :
            return True
        if s and t and s.val == t.val :
            return (self.sameTree(s.left,t.left) and self.sameTree(s.right,t.right) )
        return False