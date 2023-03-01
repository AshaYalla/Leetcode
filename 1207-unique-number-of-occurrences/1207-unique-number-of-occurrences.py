class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dictt = dict()
        for i in arr:
            if i not in dictt:
                dictt[i] = 1
            else:
                dictt[i]+=1
        return len(set(dictt.values())) == len(dictt)
        