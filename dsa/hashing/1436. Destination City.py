class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        seen = set()
        for city in paths:
            seen.add(city[0])
        for city in paths:
            if city[1] not in seen:
                return city[1]
        