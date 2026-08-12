class Solution:
    def maxDifference(self, s: str) -> int:
        charMap = Counter(s)
        even = []
        odd = []

        for curr in charMap.values():
            #curr = charMap[key]
            if curr % 2 == 0:
                even.append(curr)
            else:
                odd.append(curr)
        return max(odd) - min(even)