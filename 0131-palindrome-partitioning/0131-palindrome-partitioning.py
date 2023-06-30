class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        def palindrome(ind,arr):
            if(ind == n ):
                ans.append(arr[:])
                return
            for i in range(ind,n):
                start = ind
                end = i
                flag = 1
                while(start <= end):
                    if s[start] != s[end]:
                        flag = 0
                        break
                    start+=1
                    end-=1
                if flag:
                    arr.append(s[ind:i+1])
                    palindrome(i+1,arr)
                    arr.pop()
        palindrome(0,[])
        return ans
    
#     class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         ans = []
#         n = len(s)

#         def backtrack(path, start):
#             if start == n:
#                 # all the characters are palindromes, add to the answer
#                 ans.append(path[:])
#                 return

#             for i in range(start + 1, n + 1):
#                 comb = s[start:i]
#                 if comb == comb[::-1]:
#                     # the current combination is a palindrome, continue exploring
#                     path.append(comb)
#                     backtrack(path, i)
#                     path.pop()
        
#         backtrack([], 0)

#         return ans

            
            
                        
            
        