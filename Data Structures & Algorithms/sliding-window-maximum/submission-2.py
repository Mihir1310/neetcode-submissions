class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dis_chars = {}
        l=0
        r=k-1
        res = []
        for i in range(k):
            dis_chars[nums[i]] = 1 + dis_chars.get(nums[i], 0) 
        res.append(max(dis_chars))

        for i in range(k, len(nums)):
            dis_chars[nums[l]] -= 1
            if dis_chars[nums[l]] == 0:
                del dis_chars[nums[l]]
            l+=1
            dis_chars[nums[i]] = 1 + dis_chars.get(nums[i], 0) 
            res.append(max(dis_chars))
        return res
