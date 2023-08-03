class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        dictt = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        ans = []
        
        def solve(i,path):
            if i == len(digits):
                ans.append(''.join(path))
                return
            for j in dictt[digits[i]]:
                path.append(j)
                solve(i+1,path)
                path.pop()
        solve(0,[])
        return ans

                
            
        