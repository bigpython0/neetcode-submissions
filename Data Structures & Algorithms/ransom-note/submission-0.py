class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1 = Counter(magazine)
        c2 = Counter(ransomNote)

        cD = c2 - c1
        return not cD