class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        l=0
        for r in range(len(s2)):
            if r + window_size <= len(s2):
                subs2 = s2[r:r+window_size]
                if sorted(subs2) == sorted(s1):
                    return True
        return False


        