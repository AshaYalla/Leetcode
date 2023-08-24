"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return node
        visited = {}
        queue = [node]
        visited[node] = Node(node.val,[])
        while queue:
            n = queue.pop(0)
            for child in n.neighbors:
                if child not in visited:
                    visited[child] = Node(child.val,[])
                    queue.append(child)
                visited[n].neighbors.append(visited[child])
        return visited[node]
                    
            
        