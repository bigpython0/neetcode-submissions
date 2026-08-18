class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pMap = {}
        for i in range(len(names)):
            pMap[heights[i]] = names[i]

        sortedPeople = sorted(pMap, key=pMap.get, reverse=True)

        return sortedPeople