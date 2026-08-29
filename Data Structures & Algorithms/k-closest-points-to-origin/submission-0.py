class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for point in points:
            x, y = point
            d = math.sqrt(x**2 + y**2)
            heapq.heappush(heap, (d, point))

        res = []
        for _ in range(k):
            d, point = heapq.heappop(heap)
            res.append(point)

        return res


        