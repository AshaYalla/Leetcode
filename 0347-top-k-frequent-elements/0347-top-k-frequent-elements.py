class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictt = dict()
        for i in nums:
            dictt[i] = 1 + dictt.get(i,0)
        print(dictt)
        return(list(dict(sorted( dictt.items(),key=lambda x:x[1],reverse=True)).keys())[:k])
        

            