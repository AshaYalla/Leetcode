class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        result = []
        for i in strs:
            d[''.join(sorted(i))].append(i)
        return d.values()
                
            
            
        