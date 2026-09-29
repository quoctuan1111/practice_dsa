class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = ans = 0
        dic = {}
        for right, char in enumerate(s):
            if char in dic and dic[char] >= left:
                left = dic[char] + 1
            dic[char] = right
            ans = max(ans, right - left + 1)
        return ans 