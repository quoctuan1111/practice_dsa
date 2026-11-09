class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        heap = []
        for num in arr:
            dis = abs(x - num)
            heapq.heappush(heap, (-dis, -num))
            if len(heap) > k:
                heapq.heappop(heap)
        return sorted([-pair[1] for pair in heap])