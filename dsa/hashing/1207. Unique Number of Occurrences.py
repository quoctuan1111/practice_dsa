class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        c = defaultdict(int)
        for num in arr:
            c[num] += 1
        freq = c.values()
        return len(set(freq)) == len(freq)