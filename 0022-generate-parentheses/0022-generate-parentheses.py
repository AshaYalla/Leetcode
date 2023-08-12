class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def solve(i,j,path):
            if i == 0 and j == 0:
                ans.append("".join(path[:]))
                return
            if i > 0:
                path += "("
                solve(i-1,j,path)
                path.pop()
            if j > i:
                path += ")"
                solve(i,j-1,path)
                path.pop()
        solve(n,n,[])
        return ans
            
                
                
            
                
        