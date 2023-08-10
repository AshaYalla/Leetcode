class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0, len(numbers) -1 
        while(i < j):
            if numbers[i] + numbers[j] == target:
                print(numbers[i] + numbers[j] , i, j)
                return [i+1,j+1]
            elif numbers[i] + numbers[j] > target:
                j-=1
            else:
                i+=1
                
        