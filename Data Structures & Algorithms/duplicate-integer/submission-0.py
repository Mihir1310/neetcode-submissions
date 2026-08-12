class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        i=0
        j=1
        while j <= len(nums)-1:
            if nums[i] == nums[j]:
                return True
            i = j
            j = j+1
        return False

