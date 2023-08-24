"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
     def cloneGraph(self, node: 'Node') -> 'Node':

        visited = {}
        def dfs(n):

            if n in visited:
                return visited[n]
            clone = Node(n.val)
            visited[n] = clone

            for nei in n.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone
        return dfs(node) if node else None
            


                    
            
        