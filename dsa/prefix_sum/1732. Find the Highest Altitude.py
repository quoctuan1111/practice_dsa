class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        prefix = [0]
        for g in gain:
            prefix.append(prefix[-1] + g)
        return max(prefix)