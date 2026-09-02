class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        used = set()  # ✓ Track which indices are used
        
        def backtrack():
            if len(subset) == len(nums):  # ✓ Compare to length
                res.append(subset.copy())
                return
            
            # ✓ Try each number
            for i in range(len(nums)):
                if i not in used:  # ✓ Skip if already used
                    subset.append(nums[i])
                    used.add(i)
                    backtrack()
                    subset.pop()  # ✓ Backtrack
                    used.remove(i)
        
        backtrack()
        return res