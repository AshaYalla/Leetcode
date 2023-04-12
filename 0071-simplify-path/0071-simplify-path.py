class Solution:
    def simplifyPath(self, path: str) -> str:
        op = []
        for i in path.split('/'):
            if i == '..':
                if op:
                    op.pop()
            elif i == '.' or i == '':
                continue
            else:
                op.append(i)
        return "/" + "/".join(op)
    
                
            
            
            
            
                
        