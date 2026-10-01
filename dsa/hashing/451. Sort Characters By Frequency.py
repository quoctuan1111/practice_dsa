class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        sorted_char = sorted(count.items(), key=lambda x: x[1], reverse=True)
        ans =[]
        for c, freq in sorted_char:
            ans.append(c * freq)
        return "".join(ans)
