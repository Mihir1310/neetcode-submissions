class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [[] for _ in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                res[i] = 1
            else:
                res[i] = res[i-1]*nums[i-1]
        post = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i]*post
            post = post*nums[i]
        return res          
            