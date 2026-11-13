class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        nums.sort()
        prefix = [0]
        for n in nums:
            prefix.append(prefix[-1] + n)
        ans = []
        for q in queries:
            best = 0
            left = 0
            right = len(prefix) - 1
            while left <= right:
                mid = (left+right) // 2
                if prefix[mid] <= q:
                    best = mid
                    left = mid + 1
                else:
                    right = mid - 1
            ans.append(best)
        return ans