class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        count = defaultdict(int)
        for char in text:
            count[char] += 1
        return min(
            count["b"],
            count["a"],
            count["l"] // 2,
            count["o"] // 2,
            count["n"]
        )
