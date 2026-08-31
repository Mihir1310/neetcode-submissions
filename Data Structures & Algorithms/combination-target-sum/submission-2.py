class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        subset = []
        total = 0
        def backtrack(i, total):
            if total == target:
                res.append(subset.copy())
                return
            if i==len(nums) or total>target:
                return
            
            backtrack(i+1, total)
            
            subset.append(nums[i])
            backtrack(i, total + nums[i])
            subset.pop()

        backtrack(0, total)
        return res