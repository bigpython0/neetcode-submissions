class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()

        lengths = []
        for i in range(len(words)):
            lengths.append(len(words[i]))
        
        return lengths[len(lengths)-1]