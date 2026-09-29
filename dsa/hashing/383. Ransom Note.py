class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count = defaultdict(int)
        for char in magazine:
            count[char] += 1
        for char in ransomNote:
            if count[char] == 0:
                return False
            count[char] -= 1
        return True