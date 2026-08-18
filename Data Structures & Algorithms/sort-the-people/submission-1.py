class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pMap = {}
        for i in range(len(names)):
            pMap[heights[i]] = names[i]

        sortedPeople = [pMap[i] for i in sorted(pMap, reverse=True)]

        return sortedPeople