class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        freq = [[] for _ in range(len(nums) + 1)]
        for i in nums:
            h[i] = 1 + h.get(i, 0)
        for key, value in h.items():
            freq[value].append(key)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res