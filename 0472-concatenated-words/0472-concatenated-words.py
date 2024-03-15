class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wset = set(words)

        @cache
        def foo(ind,s):
            w = ''
            
            for i in range(ind,len(s)):
                w+=s[i]
                if w in wset:
                    if i+1 == len(s):
                        return 1
                    result = foo(i+1,s)
                    if(result):
                        return 1+result

        ans =[]
        for s in words:
            k = s
            if(foo(0,s) > 1):
                ans.append(s)

        return ans
            
    
                
            
        