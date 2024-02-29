class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if(len(sentence1) != len(sentence2)):
            return False
        
        hashmap = defaultdict(set)
        
		# create adj list
        for x, y in similarPairs:                      
            hashmap[x].add(y)
            hashmap[y].add(x)
        
        
        def dfs(word, target, hashmap, visited):
            if(word == target):
                return True
            visited.add(word)
            for nei in hashmap[word]:
                if(nei not in visited):
                    if(dfs(nei, target, hashmap, visited)):
                        return True
            
            return False
        
        
        for i in range(len(sentence1)):
            w1, w2 = sentence1[i], sentence2[i]
			
			#foreach w1 parse through the adj list to check if the corresponding word is present
            if(w1 != w2 and not dfs(w1, w2, hashmap, set())):
                return False
        
        return True
        
        
        
        
        
        
        
        
        
        
        
        
#         if len(sentence1) != len(sentence2):
#             return False
        
#         parent = [i for i in range(len(similarPairs))]
        
#         def findp(x):
#             while(parent[x] != x):
#                 parent[x] = parent[parent[x]]
#                 x = parent[x]
#             return x
#         def union(i,j):
#             parent[findp(i)] = findp(j)
        
#         dictt = defaultdict(int)
        
#         for idx, [i,j] in enumerate(similarPairs):
#             if i in dictt:
#                 union(idx, dictt[i])
#             else:
#                 dictt[i] = idx
#             if j in dictt:
#                 union(idx, dictt[j])
#             else:
#                 dictt[j] = idx
#         simdic = defaultdict(list)
#         for i,j in similarPairs:
#             simdic[i].append(j)
#             simdic[j].append(i)

#         for i in range(len(sentence1)):
#             if sentence1[i] == sentence2[i] or sentence2[i] in simdic[sentence1[i]]:
#                 continue
#             if sentence2[i] in dictt and sentence1[i] in dictt and findp(dictt[sentence2[i]]) == findp(dictt[sentence1[i]]):
#                 continue
#             return False
#         return True
            
        
