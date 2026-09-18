class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        n = len(s_list)
        start = 0
        for end in range(n + 1):
            if end == n or s_list[end] == " ":
                left, right = start, end - 1
                while left < right:
                    s_list[left], s_list[right] = s_list[right], s_list[left]
                    left += 1
                    right -= 1
                start = end + 1
        return "".join(s_list)



