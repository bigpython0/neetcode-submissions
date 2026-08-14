class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pMap = Counter(path)
        print(pMap)

        for val in pMap:
            if pMap[val] > 1:
                return True

        return False