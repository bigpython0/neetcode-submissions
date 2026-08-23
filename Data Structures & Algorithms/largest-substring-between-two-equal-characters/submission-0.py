class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        cMap = Counter(s)
        cMap = {k: v for k, v in cMap.items() if v % 2 == 0}
        maxL = -1

        for c in cMap:
            l = -1
            r = -1
            for i in range(len(s)):
                if s[i] == c and l == -1:
                    l = i
                elif s[i] == c:
                    r = i
                    maxL = max(maxL, r-l - 1)
        
        return maxL 
                