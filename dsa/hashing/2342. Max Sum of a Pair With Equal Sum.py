class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        group = defaultdict(list)
        for num in nums:
            digit_sum = 0
            for digit in str(num):
                digit_sum += int(digit)
            group[digit_sum].append(num)
        ans = -1
        for arr in group.values():
            if len(arr) >= 2:
                arr.sort(reverse=True)
                ans = max(ans, arr[0] + arr[1])
        return ans