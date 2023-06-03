class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj_matrix = defaultdict(list)
        for i in range(len(manager)):
            if manager[i] == -1:
                continue
            adj_matrix[manager[i]].append(i)
    
        time = 0
        stack = [(headID, informTime[headID])]
        while(stack):
            node_manager, curr_time = stack.pop()
            for node_subordinate in adj_matrix[node_manager]:
                new_time = curr_time + informTime[node_subordinate]
                time = max(time, new_time)
                stack.append((node_subordinate, new_time))
        return time
            
            
        
            
        