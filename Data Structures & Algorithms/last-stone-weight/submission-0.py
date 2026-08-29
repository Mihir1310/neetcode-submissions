class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            a1 = -heapq.heappop(stones)
            a2 = -heapq.heappop(stones)

            diff = a1-a2

            heapq.heappush(stones, -diff)

        return -stones[0]

        