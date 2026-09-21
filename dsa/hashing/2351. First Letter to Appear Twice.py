class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        seen = set()
        for char in s:
            if char in seen:
                return char
            seen.add(char)
        return ""  # Return an empty string if no character is repeated