class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        seen = set()
        for char in sentence:
            seen.add(char)
            if len(seen) == 26:
                return True
        return False

