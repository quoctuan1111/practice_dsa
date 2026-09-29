class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        s = set(jewels)
        count = 0
        for char in stones:
            if char in s:
                count += 1
        return count