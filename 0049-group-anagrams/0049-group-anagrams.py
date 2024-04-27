class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         dictt = defaultdict(list)
        
#         for word in strs:
#             dictt[tuple(sorted(word))].append(word)
#         return dictt.values()
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
    
#dictt keys should be hashable cant use set or list
# tuple values cant be changed is immutable hence hashable 
#frozenset is also hashable but cant be used as set removes duplciates

# t-o(n*mlogm)  s- o(n)
# t-o(n*m) s-o(n*m)