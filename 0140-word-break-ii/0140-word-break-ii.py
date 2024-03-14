class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        def foo(s):
            res = []
            if not s:
                return 0
            for w in wordDict:
                w1 = s[:len(w)]
                if w == w1:
                    items = foo(s[len(w):])
                    if(items == 0):
                        res.append(w)
                    else:
                        for item in items:
                            res.append(w + " " + item)
            return res
            
        ans = foo(s)
        return ans

                
                
        