class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        lastWord = 0

        for i in range(len(s) -1, -1, -1):
            if lastWord > 0 and s[i] == ' ':
                return lastWord
            elif s[i] != ' ':
                lastWord += 1
        
        return lastWord