class Solution(object):
    def halveArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target = sum(nums) / 2.0
        heap = [-num for num in nums]
        heapq.heapify(heap)
        ans = 0
        while target > 0:
            x = heapq.heappop(heap)

            reduced = abs(x) / 2.0
            target -= reduced

            heapq.heappush(heap, x / 2.0)
            ans += 1    
        return ans