class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dictt = dict()
        for i in matches:
            if i[1] in dictt:
                dictt[i[1]]+=1
            else:
                dictt[i[1]]=1
            if i[0] not in dictt:
                dictt[i[0]] = 0
                
        result = [[],[]]
        for i in sorted(dictt.items()):
            if i[1] ==0:
                result[0].append(i[0])
            if i[1] ==1:
                result[1].append(i[0])
        return result
            
            
        