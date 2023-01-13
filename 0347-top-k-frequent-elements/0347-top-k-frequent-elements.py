class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for i in range( len(nums)+1)]
        res = []
        dictt = dict()
        for i in nums:
            dictt[i] = 1 + dictt.get(i,0)
            
        for a,b in dictt.items():
            arr[b].append(a)
            
        for i in range(len(arr) - 1, 0, -1):
            for j in arr[i]:
                res.append(j)
                if(len(res) == k):
                    return res
                       
            
            
            
        # dictt = dict()
        # for i in nums:
        #     dictt[i] = 1 + dictt.get(i,0)
        # print(dictt)
        # return(list(dict(sorted( dictt.items(),key=lambda x:x[1],reverse=True)).keys())[:k])
        

            