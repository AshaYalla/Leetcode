

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)

        def backtrack(path, start):
            if start == n:
                # all the characters are palindromes, add to the answer
                ans.append(path[:])
                return

            for i in range(start , n):
                comb = s[start:i+1]
                if comb == comb[::-1]:
                    # the current combination is a palindrome, continue exploring
                    path.append(comb)
                    backtrack(path, i+1)
                    path.pop()

        backtrack([], 0)

        return ans

            
            
                        
            
        