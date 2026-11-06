class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        heap = [-pile for pile in piles]
        heapq.heapify(heap)
        for i in range(k):
            x = heapq.heappop(heap)
            remain = abs(x) - abs(x) // 2
            heapq.heappush(heap, -remain)
        return -sum(heap)
            