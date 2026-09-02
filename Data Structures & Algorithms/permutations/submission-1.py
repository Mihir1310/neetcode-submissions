class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(first=0):
            if first == len(nums):
                res.append(nums[:])  # ✓ Copy current permutation
                return
            
            for i in range(first, len(nums)):
                # ✓ Swap
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                # ✓ Swap back
                nums[first], nums[i] = nums[i], nums[first]
        
        backtrack()
        return res