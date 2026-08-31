class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def bt_dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # What choices I have?
            # Option 1 : Include nums[i]
            subset.append(nums[i])    
            bt_dfs(i+1)
            
            # Option 2: Not include nums[i]
            subset.pop()
            bt_dfs(i+1) 
        bt_dfs(0)
        return res