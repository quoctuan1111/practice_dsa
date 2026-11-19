class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans = []

        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def bt(index, path):
            if index == len(digits):
                ans.append("".join(path))
                return
            letters = phone[digits[index]]
            for letter in letters:
                path.append(letter)
                bt(index + 1 ,path)
                path.pop()
        bt(0, [])
        return ans

           