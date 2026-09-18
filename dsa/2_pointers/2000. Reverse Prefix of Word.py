class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        right = word.find(ch)
        if word[right] == -1:
            return word
        left = 0
        s_l= list(word)
        while left < right:
            s_l[left], s_l[right] = s_l[right], s_l[left]
            left += 1
            right -= 1
        return "".join(s_l)
