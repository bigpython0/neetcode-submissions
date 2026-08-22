class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        countedOdd = False
        sMap = Counter(s)

        for c in sMap:
            if sMap[c] % 2 == 0:
                count += sMap[c]
            else:
                if not countedOdd:
                    print(count)
                    count +=1
                    countedOdd = True
        
        return count
