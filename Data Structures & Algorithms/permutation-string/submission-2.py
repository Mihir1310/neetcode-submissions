class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        hash_s1 = {}
        hash_s2 = {}
        l = 0

        for s in s1:
            hash_s1[s] = 1 + hash_s1.get(s, 0)

        for r in range(len(s2)):
            hash_s2[s2[r]] = 1 + hash_s2.get(s2[r], 0)
            if r-l+1<len(s1):
                continue
            else:
                if hash_s1 == hash_s2:
                    return True
                else:
                    hash_s2[s2[l]] -= 1
                    if hash_s2[s2[l]] == 0:
                        del hash_s2[s2[l]]
                    l+=1
        return False  