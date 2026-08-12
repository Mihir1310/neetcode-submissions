class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        li = list(h.values())
        li.sort(reverse=True)
        res = list()
        for i in range(k):
            for key, value in h.items():
                if value == li[i]:
                    res.append(key)
                    h[key] = -1
                    break
        return res
