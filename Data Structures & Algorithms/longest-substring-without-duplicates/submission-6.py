class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        l=0
        s = set()
        res=0
        for r in range(len(string)):
            while string[r] in s:
                s.remove(string[l])
                l+=1
            s.add(string[r])   
            res = max(res, r-l+1)
        return res   
