class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        x, y = 0, 0
        seen = {(0,0)}
        for direction in path:
            if direction == "N":
                y += 1
            elif direction == "S":
                y -= 1
            elif direction == "E":
                x += 1
            elif direction == "W":
                x -= 1
                
            if (x, y) in seen:
                return True
            seen.add((x, y))
        return False