class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        matrix = Counter(nums)
        ans = []
        while(any(value != 0 for value in matrix.values())):
            arr = []
            for i in matrix:
                if matrix[i]!=0:
                    arr.append(i)
                    matrix[i]-=1
            ans.append(arr)
        return ans
            
                
            
        