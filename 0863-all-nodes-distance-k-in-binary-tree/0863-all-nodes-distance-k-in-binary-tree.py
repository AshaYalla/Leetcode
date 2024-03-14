# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        queue = [root]
        while(queue):
            node = queue.pop(0)
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                queue.append(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                queue.append(node.right)
        
        visited = set([target])
        res = []
        queue = [(target,0)]
        while queue:
            node,distance = queue.pop(0)
            if distance == k:
                res.append(node.val)
            else:
                for i in graph[node]:
                    if i not in visited:
                        visited.add(i)
                        queue.append((i,distance+1))
        return res
       
            

            
                
                
                