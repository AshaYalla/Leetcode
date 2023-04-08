"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
    
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        new = dict()
        new[node] = Node(node.val, [])
        queue = [node]
        while(queue):
            popp = queue.pop(0)
            for i in popp.neighbors:
                if i not in new:
                    new[i] = Node(i.val,[])
                    queue.append(i)
                new[popp].neighbors.append(new[i])
                
        return new[node]
            
            
            
            
        