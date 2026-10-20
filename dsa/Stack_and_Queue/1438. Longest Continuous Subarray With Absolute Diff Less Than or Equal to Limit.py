class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        increase = deque()
        decrease = deque()
        left = ans = 0

        for right in range(len(nums)):
            while increase and increase[-1] > nums[right]:
                increase.pop()
            while decrease and decrease[-1] < nums[right]:
                decrease.pop()
            increase.append(nums[right])
            decrease.append(nums[right])

            while decrease[0] - increase[0] > limit:
                if nums[left] == decrease[0]:
                    decrease.popleft()
                if nums[left] == increase[0]:
                    increase.popleft()  
                left += 1
            ans = max(ans, right - left + 1)
        return ans
