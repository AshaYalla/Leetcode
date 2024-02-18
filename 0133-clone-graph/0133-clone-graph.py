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
                return node
            dictt = {}
            qu = [node]
            visited = set()
            while qu:
                n = qu.pop(0)
                if n.val not in visited:
            
                    if n not in dictt:

                        dictt[n] = Node(n.val,[])
                    for i in n.neighbors:
                        if i not in dictt:
                            dictt[i] = Node(i.val,[])
                            qu.append(i)
                        dictt[n].neighbors.append(dictt[i])
                    visited.add(n.val)
            return dictt[node]
 
            
#         visited = {}
#         def dfs(n):
#             if n in visited:
#                 return visited[n]
#             clone = Node(n.val)
#             visited[n] = clone

#             for nei in n.neighbors:
#                 clone.neighbors.append(dfs(nei))
#             return clone
#         return dfs(node) if node else None
            
    # def cloneGraph(self, node: 'Node') -> 'Node':
    # if not node:
    #     return None
    # visited = {}
    # visited[node] = Node(node.val,[])
    # queue = [node]
    # while(queue):
    #     first = queue.pop(0)
    #     for n in first.neighbors:
    #         if n not in visited:
    #             queue.append(n)
    #             visited[n] = Node(n.val,[])   
    #         visited[first].neighbors.append(visited[n])
    # return(visited[node])


                    
            
        