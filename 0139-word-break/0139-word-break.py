class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.ans = False
        @cache
        
        def w_break(s):
            if(len(s) == 0):
                self.ans =  True
                return
            for i in wordDict:
                if(s[:len(i)] == i):
                    w_break(s[len(i):])
        
        w_break(s)
        return self.ans

                    
            
                