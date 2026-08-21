class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l<r:
            m = (r+l)//2
            time = 0
            for b in piles:
                time = time + math.ceil(b/m)
            if time > h:
                l = m + 1
            elif time <= h:
                r = m 
        return l
