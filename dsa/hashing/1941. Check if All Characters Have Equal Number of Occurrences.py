class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count = defaultdict(int)
        for char in s:
            count[char] += 1
        freq = count.values()
        return len(set(freq)) == 1