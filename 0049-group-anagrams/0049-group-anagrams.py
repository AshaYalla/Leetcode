class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt = defaultdict(list)
        
        for word in strs:
            dictt[tuple(sorted(word))].append(word)
        return dictt.values()
    
#dictt keys should be hashable cant use set or list
# tuple values cant be changed is immutable hence hashable 
#frozenset is also hashable but cant be used as set removes duplciates