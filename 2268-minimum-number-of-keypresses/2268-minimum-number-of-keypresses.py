class Solution:
    def minimumKeypresses(self, s: str) -> int:
        dictt = defaultdict(int)
        for i in s:
            dictt[i]+=1
        ans = 0
        for i,val in enumerate(sorted(dictt.values(), reverse = True)):
            ans += (i // 9 + 1) * val
        return ans
    
# class Solution:
#     def minimumKeypresses(self, s: str) -> int:
#         c = collections.Counter(s)
#         ans = cnt = 0
#         for i, freq in enumerate(sorted(c.values(), reverse=True)):  # sort reversely
#             if i % 9 == 0:
#                 cnt += 1
#             ans += cnt * freq                                        # add `num_of_time_to_press_the_key * frequency` to result
#         return ans
            
            
            
            
            
            
            
            
            