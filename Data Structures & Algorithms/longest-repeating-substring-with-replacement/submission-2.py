class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countMap = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(s)):
            countMap[s[r]] += 1
            if r-l+1-max(countMap.values()) > k:
                countMap[s[l]]-=1
                l+=1
            else:
                res = max(res, r-l+1)
        return res        