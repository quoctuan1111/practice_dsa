class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        count = defaultdict(int)
        for arr in nums:
            for x in arr:
                count[x] += 1
        
        n = len(nums)
        ans = []
        for x in count:
            if count[x] == n:
                ans.append(x)
        return sorted(ans)