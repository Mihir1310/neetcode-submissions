class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for n in nums:
            if n-1 in nums:
                continue
            temp_max = 1
            while n+1 in nums:
                temp_max += 1
                n += 1
            res = max(temp_max, res)
        return res
                
            