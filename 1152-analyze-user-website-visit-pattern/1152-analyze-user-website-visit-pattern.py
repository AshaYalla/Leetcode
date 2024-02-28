class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        mp = {}
        for t, u, w in sorted(zip(timestamp, username, website)): 
            mp.setdefault(u, []).append(w)
        
        freq = defaultdict(int)
        for key, val in mp.items(): 
            seen = set()
            for i in range(len(val)):
                for j in range(i+1, len(val)):
                    for k in range(j+1, len(val)): 
                        seen.add((val[i], val[j], val[k]))
            for x in seen: freq[x] += 1
        
        return min(freq, key=lambda x: (-freq[x], x))
        
        
        
        
        
        
#         hmap = collections.defaultdict(list)
#         N = len(username)
#         for i in range(N):
#             hmap[username[i]].append((timestamp[i], website[i]))

#         def get_pattern(websites):
#             res = []
#             def dfs(idx, path):
#                 if len(path) == 3:
#                     res.append(path[:])
#                     return

#                 for i in range(idx + 1, len(websites)):
#                     path.append(websites[i][1])
#                     dfs(i, path)
#                     path.pop()

#             dfs(-1, [])
#             return res

#         pattern_map = {}
#         for websites in hmap.values():
#             websites.sort()
#             memo = set() # to avoid the same pattern getting added multiple times
#             for pattern in get_pattern(websites):
#                 k = tuple(pattern)
#                 if k not in memo:
#                     pattern_map[k] = pattern_map.get(k, 0) + 1
#                     memo.add(k)
        
#         return max(sorted(pattern_map), key=pattern_map.get)

# class Solution:
#     def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
#         users = defaultdict(list)
#         for user, time, site in sorted(zip(username, timestamp, website), key = lambda x:(x[0],x[1])):
#             users[user].append(site)
#         patterns = Counter()
#         for user, sites in users.items():
#             patterns.update(Counter(set(combinations(sites, 3))))
#         return max(sorted(patterns), key = lambda x: patterns[x])