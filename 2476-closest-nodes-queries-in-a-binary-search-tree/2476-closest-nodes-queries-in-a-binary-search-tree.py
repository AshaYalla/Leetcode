# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        
        nums = []
        def inorder(node):
            if node:
                inorder(node.left)
                nums.append(node.val)
                inorder(node.right)
        inorder(root)        
        
        n = len(nums)
        
        ans = []
        for target in queries:
            ans.append([-1, -1])
            
            l, r = 0, n-1
            while l <= r:
                mid = l + (r - l)//2
                
                if nums[mid] == target:
                    ans[-1] = [target, target]
                    break
                elif nums[mid] > target:
                    ans[-1][1] = nums[mid]
                    r = mid -1
                else:
                    ans[-1][0] = nums[mid]
                    l = mid + 1
            
        return ans    