class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def combi(tar, comb, start):
            if tar == 0:
                if comb not in ans and len(comb) == k:
                    ans.append(list(comb))
                return
            elif tar < 0:
                return 
            for i in range(start,10):
                comb.append(i)
                combi(tar - i,comb,i+1)
                comb.pop()
        combi(n,[],1)
        return ans