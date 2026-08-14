class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        hash_t = {}
        window = {}
        have, need = 0, len(t)
        l=0
        res, reslen = [-1, -1], float("inf")

        for ts in t:
            hash_t[ts] = 1 + hash_t.get(ts, 0)
        have, need = 0, len(hash_t)
        
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in t and window[s[r]] == hash_t[s[r]]:
                have += 1

            while have == need:
                if (r-l+1) < reslen:
                    res = [l, r]
                    reslen = r-l+1 
                window[s[l]] -= 1
                if s[l] in t and window[s[l]] < hash_t[s[l]]:
                    have -= 1
                l+=1
        l,r = res
        return s[l: r+1] if (r-l+1)!=float("inf") else ""       