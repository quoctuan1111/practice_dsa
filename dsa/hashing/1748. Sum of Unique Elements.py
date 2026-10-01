class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        sum = 0
        for num, freq in count.items():
            if freq == 1:
                sum += num
        return sum