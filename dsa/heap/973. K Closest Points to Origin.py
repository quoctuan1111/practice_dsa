class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        for point in points:
            x, y = point
            dis = x*x + y*y
            heapq.heappush(heap, (-dis, point))
            if len(heap) > k:
                heapq.heappop(heap)
        return [pair[1] for pair in heap]